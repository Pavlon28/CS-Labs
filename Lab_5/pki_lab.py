import os
import argparse
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.serialization import (
    load_pem_private_key,
    Encoding,
    PrivateFormat,
    NoEncryption,
)
from cryptography import x509
from cryptography.x509 import NameOID, CertificateBuilder
from datetime import datetime, timedelta, timezone


# Directories
BASE_DIR = "pki_lab"
CA_DIR = os.path.join(BASE_DIR, "ca")
USERS_DIR = os.path.join(BASE_DIR, "users")
REVOKED_DIR = os.path.join(BASE_DIR, "revoked")


def setup_directories():
    os.makedirs(CA_DIR, exist_ok=True)
    os.makedirs(USERS_DIR, exist_ok=True)
    os.makedirs(REVOKED_DIR, exist_ok=True)


def generate_ca():
    print("Setting up CA...")

    # Generate a private key for the CA
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096)
    with open(os.path.join(CA_DIR, "ca_key.pem"), "wb") as key_file:
        key_file.write(
            private_key.private_bytes(
                encoding=Encoding.PEM,
                format=PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=NoEncryption(),
            )
        )

    # Define the subject and issuer using x509.Name and NameAttribute
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "State"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "City"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Organization"),
        x509.NameAttribute(NameOID.COMMON_NAME, "RootCA"),
    ])

    # Create a self-signed certificate for the CA
    cert = (
        CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())  # Corrected serial number generation
        .not_valid_before(datetime.now(timezone.utc))  # Updated to use timezone-aware datetime
        .not_valid_after(datetime.now(timezone.utc) + timedelta(days=3650))  # Valid for 10 years
        .sign(private_key, hashes.SHA256())
    )

    # Save the certificate
    with open(os.path.join(CA_DIR, "ca_cert.pem"), "wb") as cert_file:
        cert_file.write(cert.public_bytes(Encoding.PEM))

    print("CA setup complete.")


def generate_user_certificate(username):
    print(f"Generating certificate for user {username}...")
    user_dir = os.path.join(USERS_DIR, username)
    os.makedirs(user_dir, exist_ok=True)

    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    with open(os.path.join(user_dir, "user_key.pem"), "wb") as key_file:
        key_file.write(
            private_key.private_bytes(
                encoding=Encoding.PEM,
                format=PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=NoEncryption(),
            )
        )

    ca_private_key_path = os.path.join(CA_DIR, "ca_key.pem")
    ca_cert_path = os.path.join(CA_DIR, "ca_cert.pem")
    with open(ca_private_key_path, "rb") as key_file:
        ca_private_key = load_pem_private_key(key_file.read(), password=None)

    with open(ca_cert_path, "rb") as cert_file:
        ca_cert = x509.load_pem_x509_certificate(cert_file.read())

    subject = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "State"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "City"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Organization"),
        x509.NameAttribute(NameOID.COMMON_NAME, username),
    ])
    user_cert = (
        CertificateBuilder()
        .subject_name(subject)
        .issuer_name(ca_cert.subject)
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.now(timezone.utc))
        .not_valid_after(datetime.now(timezone.utc) + timedelta(days=365))
        .sign(ca_private_key, hashes.SHA256())
    )

    with open(os.path.join(user_dir, "user_cert.pem"), "wb") as cert_file:
        cert_file.write(user_cert.public_bytes(Encoding.PEM))
    print(f"Certificate for user {username} created.")


def sign_file(user_key_path, file_path):
    print(f"Signing file {file_path}...")
    with open(user_key_path, "rb") as key_file:
        private_key = load_pem_private_key(key_file.read(), password=None)

    with open(file_path, "rb") as f:
        file_data = f.read()

    signature = private_key.sign(file_data, padding.PKCS1v15(), hashes.SHA256())
    signature_path = f"{file_path}.sig"
    with open(signature_path, "wb") as sig_file:
        sig_file.write(signature)
    print(f"File signed. Signature saved at {signature_path}")


def verify_signature(user_cert_path, file_path, signature_path):
    print(f"Verifying signature for {file_path}...")
    with open(user_cert_path, "rb") as cert_file:
        cert = x509.load_pem_x509_certificate(cert_file.read())

    with open(file_path, "rb") as f:
        file_data = f.read()

    with open(signature_path, "rb") as sig_file:
        signature = sig_file.read()

    try:
        cert.public_key().verify(signature, file_data, padding.PKCS1v15(), hashes.SHA256())
        print("Signature verification successful.")
    except Exception:
        print("Signature verification failed.")


def revoke_certificate(user_cert_path):
    print(f"Revoking certificate from {user_cert_path}...")
    revoked_path = os.path.join(REVOKED_DIR, os.path.basename(user_cert_path))
    os.rename(user_cert_path, revoked_path)
    print(f"Certificate revoked and stored at {revoked_path}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PKI Lab Utility")
    subparsers = parser.add_subparsers(dest="command")

    # Setup CA
    subparsers.add_parser("setup_ca", help="Setup the Certificate Authority (CA)")

    # Generate User Certificate
    gen_user = subparsers.add_parser("generate_user", help="Generate a user certificate")
    gen_user.add_argument("username", type=str, help="Username for the certificate")

    # Sign a File
    sign_file_parser = subparsers.add_parser("sign_file", help="Sign a file")
    sign_file_parser.add_argument("user_key", type=str, help="Path to the user's private key")
    sign_file_parser.add_argument("file_path", type=str, help="Path to the file to sign")

    # Verify a Signature
    verify_sig_parser = subparsers.add_parser("verify_signature", help="Verify a file signature")
    verify_sig_parser.add_argument("user_cert", type=str, help="Path to the user's certificate")
    verify_sig_parser.add_argument("file_path", type=str, help="Path to the file to verify")
    verify_sig_parser.add_argument("signature", type=str, help="Path to the signature file")

    # Revoke a Certificate
    revoke_cert_parser = subparsers.add_parser("revoke_cert", help="Revoke a user's certificate")
    revoke_cert_parser.add_argument("cert_path", type=str, help="Path to the certificate to revoke")

    args = parser.parse_args()

    if args.command == "setup_ca":
        setup_directories()
        generate_ca()
    elif args.command == "generate_user":
        generate_user_certificate(args.username)
    elif args.command == "sign_file":
        sign_file(args.user_key, args.file_path)
    elif args.command == "verify_signature":
        verify_signature(args.user_cert, args.file_path, args.signature)
    elif args.command == "revoke_cert":
        revoke_certificate(args.cert_path)
    else:
        parser.print_help()