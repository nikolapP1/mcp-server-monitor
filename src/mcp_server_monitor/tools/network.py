"""Network monitoring tools."""

import socket


def check_port(host: str = "localhost", port: int = 80, timeout: float = 3.0) -> str:
    """Check if a TCP port is open on a host.

    Args:
        host: The hostname or IP to check (default: localhost).
        port: The TCP port number to check (default: 80).
        timeout: Connection timeout in seconds (default: 3).

    Returns:
        Whether the port is open or closed.
    """
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return (
                f"Host: {host}\n"
                f"Port: {port}\n"
                f"Status: OPEN\n"
                f"Connection: successful"
            )
    except socket.timeout:
        return (
            f"Host: {host}\n"
            f"Port: {port}\n"
            f"Status: TIMEOUT\n"
            f"Connection: timed out after {timeout}s"
        )
    except ConnectionRefusedError:
        return (
            f"Host: {host}\n"
            f"Port: {port}\n"
            f"Status: CLOSED\n"
            f"Connection: refused"
        )
    except OSError as e:
        return (
            f"Host: {host}\n"
            f"Port: {port}\n"
            f"Status: ERROR\n"
            f"Error: {e}"
        )
