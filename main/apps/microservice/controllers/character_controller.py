from fastapi import APIRouter

router = APIRouter()

@router.get("/characters", tags=["Characters"])
async def get_characters():
    """
    Retorna uma lista de characters.
    """
    characters = [
        {"id": 1, "name": "Character 1"},
        {"id": 2, "name": "Character 2"},
        {"id": 3, "name": "Character 3"}
    ]
    return characters

@router.get("/characters/{character_id}", tags=["Characters"])
async def get_character(character_id: int):
    """
    Retorna um character específico com base no ID fornecido.
    """
    character = {"id": character_id, "name": f"Character {character_id}"}
    return character

@router.post("/characters", tags=["Characters"])
async def create_character(character: dict):
    """
    Cria um novo character com base nos dados fornecidos.
    """
    # Lógica para criar um novo character
    return character

@router.put("/characters/{character_id}", tags=["Characters"])
async def update_character(character_id: int, character: dict):
    """
    Atualiza um character existente com base no ID fornecido e nos dados fornecidos.
    """
    # Lógica para atualizar o character
    return character

@router.delete("/characters/{character_id}", tags=["Characters"])
async def delete_character(character_id: int):
    """
    Exclui um character existente com base no ID fornecido.
    """
    # Lógica para excluir o character
    return {"message": "Character deleted"}
