#!/usr/bin/env bash

# Set Subject fields for CA and Server to avoid CN conflict
CA_SUBJECT="/C=US/ST=California/L=LosAngeles/O=IT/OU=mininetOrg/CN=Mininet-CA/emailAddress=mininet@gmail.com"
SERVER_SUBJECT="/C=US/ST=California/L=LosAngeles/O=IT/OU=mininetOrg/CN=mininet.org/emailAddress=mininet@gmail.com"

# Step 1: Create the CA Key and Self-Signed Certificate
openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:4096 -keyout ca.key -out ca.crt -subj "$CA_SUBJECT"

# Step 2: Create the Server Key and CSR
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr -subj "$SERVER_SUBJECT"

# Step 3: Sign the Server Certificate with CA
openssl x509 -req -days 365 -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -sha256

# Step 4: Verify Server Certificate
openssl verify -purpose sslserver -CAfile ca.crt server.crt

# Step 5: Create the Client Key and CSR
openssl genrsa -out client.key 2048
openssl req -new -key client.key -out client.csr -subj "$SERVER_SUBJECT"

# Step 6: Sign the Client Certificate with CA
openssl x509 -req -days 31 -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -sha256

# Step 7: Verify Client Certificate
openssl verify -purpose sslclient -CAfile ca.crt client.crt

# Step 8: Verify Server Certificate
openssl verify -purpose sslserver -CAfile ca.crt server.crt
