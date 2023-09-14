import reflex as rx

class ReflextestConfig(rx.Config):
    pass

config = ReflextestConfig(
    app_name="reflex_test",
    backend_host="18.185.100.254",
    port=3000,
)