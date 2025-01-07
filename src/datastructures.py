
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    # Método interno para generar un ID único
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    # Agregar un miembro
    def add_member(self, member):
        if 'id' not in member:
            member['id'] = self._generate_id()  # Genera un ID único si no se proporciona
        self._members.append(member)

    # Eliminar un miembro por ID
    def delete_member(self, id):
        self._members = [member for member in self._members if member['id'] != id]

    # Actualizar un miembro por ID
    def update_member(self, id, updated_member):
        for index, member in enumerate(self._members):
            if member['id'] == id:
                # Actualiza los datos del miembro
                self._members[index] = {**member, **updated_member}
                return self._members[index]
        return None  # Devuelve None si el miembro no se encuentra

    # Obtener un miembro por ID
    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member
        return None

    # Obtener todos los miembros
    def get_all_members(self):
        return self._members
