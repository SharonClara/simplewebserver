from http.server import HTTPServer,BaseHTTPRequestHandler

content="""

<!DOCTYPE html>
<html>
<head>
    <title >TCP/IP Layers and Protocols</title>
    
        
</head>
<body>
    <h2>TCP/IP Layers and Protocols</h2>
    <table border="1" cellpadding="10" align ="center">
        <tr>
            <th>TCP/IP Layers</th>
            <th>Protocols </th>
        </tr>
        <tr>
            <td>Application Layer</td>
            <td>HTTP, DNS, SMTP, Telnet</td>
        </tr>
        <tr>
            <td>Transport Layer</td>
            <td>TCP, UDP</td>
        </tr>
        <tr>
            <td>Internet Layer</td>
            <td>IPv4,IPv6</td>
        </tr>
        <tr>
            <td>Link Layer</td>
            <td>Ethernet (IEEE 802.3), MAC</td>
        </tr>
    </table>
</body>
</html>
"""

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("my webserver is running...") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()