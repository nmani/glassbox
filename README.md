# Unofficial Glassbox API
An unofficial, opinionated API for Glassbox

## Quick Start
```bash
pip install git+https://github.com/nmani/glassbox.git@devel
```

```python
from glassbox import GlassboxClient

client = GlassboxClient(
    baseurl = "https://glassbox.instance.local,
    credentals = ("username", "password")
)

sessions = client.sessions(
    session="",
    start_timestamp="",
    end_timestamp=""
    )

```

GlassboxClient will automatically check and resolve proxy enviromental variables when not using a transparent proxy but if you wish to manually specify/override proxy values.

```python
from glassbox import GlassboxClient

proxies = {
    'http': 'http://user:password@proxy.local',
    'https': 'http://user:password@proxy.local'
}

client = GlassboxClient(
    baseurl = "https://glassbox.instance.local,
    credentals = ("username", "password"), 
    proxy = proxies
)

sessions = client.sessions(
    session="",
    start_timestamp=datetime(),
    end_timestamp=""
    )

```

## Configuration

ENV variables always override stored configuration parameters

### Method #1: Environment Variables
Linux/MacOS:
```bash
export GLASSBOX_BASEURL=${}

```
Windows:
```powershell
set GLASSBOX_BASEURL=""
```

### Method #2: Configuration YAML (Recommended)
Checks for a .glassbox.yaml file in the following home locations:
Windows:


Linux:
$HOME/.glassbox.conf
$HOME/.config/glassbox/.glassbox.conf

Override it with the following value:
GLASSBOX_CONF=""