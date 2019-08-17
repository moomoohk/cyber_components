from ipaddress import ip_network, ip_interface

from sqlalchemy import TypeDecorator, Unicode
from sqlalchemy_utils.types.scalar_coercible import ScalarCoercible


class IPNetworkType(TypeDecorator, ScalarCoercible):
    impl = Unicode(50)

    def __init__(self, max_length=50, *args, **kwargs):
        super(IPNetworkType, self).__init__(*args, **kwargs)

        self.impl = Unicode(max_length)

    def process_bind_param(self, value, dialect):
        return str(value) if value else None

    def process_literal_param(self, value, dialect):
        return str(value) if value else None

    def process_result_value(self, value, dialect):
        return ip_network(value) if value else None

    def _coerce(self, value):
        return ip_network(value) if value else None

    @property
    def python_type(self):
        return self.impl.type.python_type


class IPInterfaceType(TypeDecorator, ScalarCoercible):
    impl = Unicode(50)

    def __init__(self, max_length=50, *args, **kwargs):
        super(IPInterfaceType, self).__init__(*args, **kwargs)

        self.impl = Unicode(max_length)

    def process_bind_param(self, value, dialect):
        return str(value) if value else None

    def process_literal_param(self, value, dialect):
        return str(value) if value else None

    def process_result_value(self, value, dialect):
        return ip_interface(value) if value else None

    def _coerce(self, value):
        return ip_interface(value) if value else None

    @property
    def python_type(self):
        return self.impl.type.python_type
