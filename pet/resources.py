from flask_restful import Resource

# PetList
# shows a list of all pets, and lets you POST to add new pets
class PetList(Resource):
    def get(self):
        PETS = [
            {
              "photo": "https://img-aws.ehowcdn.com/600x600p/photos.demandstudios.com/getty/article/165/76/87490163.jpg",
              "name": "Pepe",
              "species": "Cat",
              "description": "Peter is very kind, and it loves to jump over the fences and get stuck."
            },
            {
              "photo": "https://vetstreet.brightspotcdn.com/dims4/default/0cb080e/2147483647/thumbnail/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2F97%2F78%2Fdca5c3e34bb89c4e5d19a0851f5d%2Fshih-tzu-ap-1v4u0w-645-x-380.jpg",
              "name": "Neymar",
              "species": "Dog",
              "description": "Neymar is very kind, and it loves to throw its own fleas to people passing by."
            },
            {
              "photo": "https://i.amz.mshcdn.com/U1RyN-qN37YancYwWCGLfNi4x_0=/950x534/filters:quality(90)/https%3A%2F%2Fblueprint-api-production.s3.amazonaws.com%2Fuploads%2Fcard%2Fimage%2F763457%2Fb38cea03-afe1-4850-902d-9789540a7b57.jpg",
              "name": "Daniella",
              "species": "Parrot",
              "description": "Daniella is very kind, and it loves to sing politically-wrong songs."
            }
        ]
        return PETS
