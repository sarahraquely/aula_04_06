class ConversorTemperatura:
  @staticmethod
  def Celsius_para_fahrenheit (c):
    if not ConversorTemperatura .__validar(c):
      raise ValueError ("valor invalido")
    else:
      return (c*9/5)+32
    
  @staticmethod
  def fahrenheit_para_celsius (f):
    if not ConversorTemperatura .__validar(f):
      raise ValueError ("valor invalido")
    else:
      return (f-32)*5/9