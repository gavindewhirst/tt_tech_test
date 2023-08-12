from routes.i_route import routesInterface

class ratings(routesInterface):
  def process_event(self, event):
    return 1, 2
