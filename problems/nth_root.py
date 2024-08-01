from loguru import logger

log = logger.debug


def root(x, n):
  """
  1 - > 
  """
  y_min, y_max, y = 0, x, 1
  while abs(y**n - x) > 0.001:
    yn = y ** n
    log((x, y, yn))
    if yn == x:
      break
    elif yn < x:
      y_min = y
    else: # yn > x
      y_max = y
    y = (y_min + y_max) / 2
    log(y)
  return round(y, 3)

# log(root(27, 3))
log(root(81, 4))
# log(root(625, 3))
