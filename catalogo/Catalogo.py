class Pelicula:

    def __init__(self, titulo, director, year):
        self.titulo = titulo
        self.director = director
        self.year = year

    def __str__(self):
        return(f"Título: '{self.titulo}', director: {self.director}, año: {self.year}")


class Catalogo:
    peliculas = []

    def addPelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def mostrarCatalogo(self):
        print("-----------------------------------------------------------------------------")
        for pelicula in self.peliculas:
            print(pelicula)
        print("-----------------------------------------------------------------------------")


pelicula1 = Pelicula("Blade Runner", "Ridle Scott", 1982)
pelicula2 = Pelicula("2001: Una odisea del espacio", "Stanley Kubrick", 1968)
pelicula3 = Pelicula("Stalker", "Andrei Tarkovsky", 1979)
pelicula4 = Pelicula("Metrólopis", "Fritz Lang", 1927)
pelicula5 = Pelicula("El muelle", "Chris Marker", 1962)
        
catalogo = Catalogo()
catalogo.addPelicula(pelicula1)
catalogo.addPelicula(pelicula2)
catalogo.addPelicula(pelicula3)
catalogo.addPelicula(pelicula4)
catalogo.addPelicula(pelicula5)

catalogo.mostrarCatalogo()

