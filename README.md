# Tor-Network-Connection
Connect Tor Python Code

1. apt-get install tor
2. apt-get install privoxy
(we need to edit our privoxy config (/etc/privoxy/config) and add the
following line -> forward-socks4a / localhost:9050 .)
3. Start tor & privoxy service
( service tor privoxy start)