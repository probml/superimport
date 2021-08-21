from datetime import datetime
build_time=datetime.now().strftime('%Y%m%d%H%M%S')

__version__ = f"0.0.2.dev1.{build_time}"