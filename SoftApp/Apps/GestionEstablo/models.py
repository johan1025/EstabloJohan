from django.db import models


# Create your models here.
class Empleado(models.Model):
    Nombre = models.CharField(max_length=50)
    APaterno = models.CharField(max_length=50)
    AMaterno = models.CharField(max_length=50)
    FechaNacimiento = models.DateField()
    SEXOS = (('F', 'FEMENINO'), ('M', 'MASCULINO'))
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='M')
    CIVIL = (('C', 'CASADO'), ('S', 'SOLTERO'))
    Estado = models.CharField(max_length=1, choices=CIVIL, default='M')

    def CADNombreCompleto(self):
        cadena = "{0} {1} {2}"
        return cadena.format( self.Nombre,self.APaterno, self.AMaterno)

    def __str__(self):
        return self.CADNombreCompleto()


class Contrato(models.Model):
    Empleado = models.ForeignKey(Empleado, null=False, blank=False, on_delete=models.CASCADE)
    FechaInicio = models.DateField()
    FechaFin = models.DateField()
    Paga = models.DecimalField(max_digits=18, decimal_places=2)
    ConCatEstadoContrato = (('A', 'ACTIVO'), ('I', 'INACTIVO'))
    Estado = models.CharField(max_length=1, choices=ConCatEstadoContrato, default='A')
    EmpCatContratoPuesto = (('A', 'ADMINISTRATIVO'), ('I', 'AYUDANTE'), ('V', 'VETERINARIO'))
    Puesto = models.CharField(max_length=1, choices=EmpCatContratoPuesto, default='A')

    def CADEmpleadoContrato(self):
        cadenaContrato = "{0}, {1}, {2}"
        return cadenaContrato.format(self.empleado, self.FechaInicio, self.Estado)


def __str__(self):
    return self.CADEmpleadoContrato()


class Veladore(models.Model):
    Empleado = models.ForeignKey(Empleado, null=False, blank=False, on_delete=models.CASCADE)
    FechaInicio = models.DateField()
    FechaFin = models.DateField()
    HoraInicio = models.TimeField()
    HoraFin = models.TimeField()
    Observacion = models.CharField(max_length=250)
    CatEstadoVelador = (('A', 'ACTIVO'), ('I', 'INACTIVO'))
    Estado = models.CharField(max_length=1, choices=CatEstadoVelador, default='A')

    def CADempleadoVelador(self):
        cadenaVelador = "{0}"
        return cadenaVelador.format(self.empleado)


def __str__(self):
    return self.CADempleadoVelador


class Area(models.Model):
    Area = models.CharField(max_length=150)
    Medidad = models.CharField(max_length=150)
    EstadoArea = (('A', 'ACTIVO'), ('I', 'INACTIVO'))
    Estado = models.CharField(max_length=1, choices=EstadoArea, default='A')

    def CADarArea(self):
        cadenaArea = "{0}"
        return cadenaArea.format(self.Area)

    def __str__(self):
        return self.CADarArea()


class Corrale(models.Model):
    Altura = models.CharField(max_length=150)
    Ancho = models.CharField(max_length=150)
    Largo = models.CharField(max_length=150)
    Area = models.ForeignKey(Area, null=False, blank=False, on_delete=models.CASCADE)
    Capacidad = models.DecimalField(max_digits=18, decimal_places=2)
    EstadoCorral = (('A', 'ACTIVO'), ('I', 'INACTIVO'))
    Estado = models.CharField(max_length=1, choices=EstadoCorral, default='A')

    def CADcorCorrales(self):
        cadenaCorral = "{0}"
        return cadenaCorral.format(self.Capacidad)

    def __str__(self):
        return self.CADcorCorrales()


class Almacene(models.Model):
    Uso = models.CharField(max_length=150)
    Capacidad = models.DecimalField(max_digits=18, decimal_places=2)
    Area = models.ForeignKey(Area, null=False, blank=False, on_delete=models.CASCADE)
    Empleado = models.ForeignKey(Empleado, null=False, blank=False, on_delete=models.CASCADE)
    estadoAlmacen = (('A', 'ACTIVO'), ('I', 'INACTIVO'))
    Estado = models.CharField(max_length=1, choices=estadoAlmacen, default='A')

    def CADalmAlmacen(self):
        cadenaAlmacen = "{0}, {1}"
        return cadenaAlmacen.format(self.Uso, self.Area)

    def __str__(self):
        return self.CADalmAlmacen()


class Proveedore(models.Model):
    Nombre = models.CharField(max_length=50)
    RFC = models.CharField(max_length=50)
    Garantia = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=10)
    Correo = models.EmailField(max_length=75)
    Direccion = models.CharField(max_length=250)
    Almacen = models.ForeignKey(Almacene, null=False, blank=False)
    estadoProveedor = (('A', 'ACTIVO'), ('I', 'INACTIVO'))
    Estado = models.CharField(max_length=1, choices=estadoProveedor, default='A')

    def CADProveedor(self):
        cadenaProveedor = "{0}, {1}"
        return cadenaProveedor.format(self.Nombre, self.RFC)

    def __str__(self):
        return self.CADProveedor()


class Animale(models.Model):
    nombre = models.CharField(max_length=50)
    Codigo = models.CharField(max_length=10)
    FNacimiento = models.DateField()
    tipoAnimal = (('V', 'VACA'), ('C', 'CABALLO'), ('B', 'BORREGA'))
    Tipo = models.CharField(max_length=1, choices=tipoAnimal, default='V')
    colorAnimal = (('N', 'NEGRO'), ('P', 'PINTO'), ('B', 'BLANCA'))
    Color = models.CharField(max_length=1, choices=colorAnimal, default='N')
    clasificacionAnimal = (('H', 'HEMBRA'), ('M', 'MACHO'))
    Clasificacion = models.CharField(max_length=1, choices=clasificacionAnimal, default='M')

    def CADAnAnimal(self):
        cadenaAnimal = "{0}, {1}"
        return cadenaAnimal.format(self.nombre, self.Codigo)

    def __str__(self):
        return self.CADAnAnimal()


class AsignacionCorrale(models.Model):
    Animal = models.ForeignKey(Animale, null=False, blank=False, on_delete=models.CASCADE)
    Corral = models.ForeignKey(Corrale, null=False, blank=False, on_delete=models.CASCADE)
    FRegistro = models.DateField()
    estadoAsignacion = (('A', 'ACTIVO'), ('I', 'INACTIVO'))
    Estado = models.CharField(max_length=1, choices=estadoAsignacion, default='A')

    def CADAsignacion(self):
        cadenaAsignacion = "{0}, {1}, {2}"
        return cadenaAsignacion.format(self.Corral, self.Animal, self.FRegistro)

    def __str__(self):
        return self.CADAsignacion()


class Establo(models.Model):
    Nombre = models.CharField(max_length=80)
    dueño = models.ForeignKey(Empleado, null=False, blank=False, on_delete=models.CASCADE)
    Medidas = models.CharField(max_length=300)
    estadoTerreno = (('A', 'ACTIVO'), ('I', 'INACTIVO'))
    EsCatEstado = models.CharField(max_length=1, choices=estadoTerreno, default='A')
    Estado = models.CharField(max_length=150)
    Municipio = models.CharField(max_length=150)
    CodigoPostal = models.CharField(max_length=150)
    Numerotelefono = models.CharField(max_length=10)
    Correo = models.EmailField(max_length=75)

    def CADEstablo(self):
        cadenaEstablo = "{0}, {1}, {2}"
        return cadenaAsignacion.format(self.Nombre, self.Municipio, self.Correo)

    def __str__(self):
        return self.CADEstablo()
