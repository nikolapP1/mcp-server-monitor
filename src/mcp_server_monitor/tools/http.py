"""HTTP endpoint health check tool."""

import httpx


def check_http_endpoint(url: str, timeout: float = 10.0) -> str:
    """Check if an HTTP endpoint is responding.

    Args:
        url: The URL to check (e.g. http://localhost:8080/health).
        timeout: Request timeout in seconds.

    Returns:
        A summary of the endpoint status including status code and response time.
    """
    try:
        response = httpx.get(url, timeout=timeout, follow_redirects=True)
        elapsed_ms = round(response.elapsed.total_seconds() * 1000, 2)
        status = "healthy" if response.status_code < 400 else "unhealthy"
        return (
            f"Endpoint: {url}\n"
            f"Status: {status} (HTTP {response.status_code})\n"
            f"Response time: {elapsed_ms}ms\n"
            f"Content-Type: {response.headers.get('content-type', 'N/A')}"
        )
    except httpx.TimeoutException:
        return f"Endpoint: {url}\nStatus: timeout after {timeout}s"
    except httpx.ConnectError as e:
        return f"Endpoint: {url}\nStatus: connection failed\nError: {e}"
    except Exception as e:
        return f"Endpoint: {url}\nStatus: error\nError: {e}"
