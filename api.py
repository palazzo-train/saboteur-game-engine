from mangum import Mangum
from api_impl import api_fast

### moved all implementation details into api_impl
app = api_fast.app

# to make it work with Amazon Lambda, we create a handler object
handler = Mangum(app=app)