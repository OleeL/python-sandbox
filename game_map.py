ROOM_MAP = {
    "hall": {
        "name": "Hall",
        "north": "kitchen",
        "south": "bedroom",
        "east": "living_room",
        "west": "bathroom",
        "description": "A spacious hallway with high ceilings and large windows.",
        "items": ["rusty_key", "golden_key"]
    },
    "kitchen": {
        "name": "Kitchen",
        "north": "dining_room",
        "south": "hall",
        "east": "pantry",
        "west": "garage",
        "description": "A well-equipped kitchen with a large island and plenty of storage space.",
        "items": []
    },
    "bedroom": {
        "name": "Bedroom",
        "north": "hall",
        "south": "bathroom",
        "east": "closet",
        "west": "office",
        "description": "A cozy bedroom with a comfortable bed and a small desk.",
        "items": []
    },
    "living_room": {
        "name": "Living Room",
        "north": "hall",
        "south": "dining_room",
        "east": "balcony",
        "west": "pantry",
        "description": "A comfortable living room with a large sofa and a coffee table.",
        "items": []
    },
    "bathroom": {
        "name": "Bathroom",
        "north": "bedroom",
        "south": "hall",
        "east": "pantry",
        "west": "garage",
        "description": "A modern bathroom with a large shower and a bathtub.",
        "items": []
    },
    "dining_room": {
        "name": "Dining Room",
        "north": "kitchen",
        "south": "living_room",
        "east": "pantry",
        "west": "garage",
        "description": "A spacious dining room with a large table and comfortable chairs.",
        "items": []
    },
    "pantry": {
        "name": "Pantry",
        "north": "kitchen",
        "south": "living_room",
        "east": "balcony",
        "west": "bathroom",
        "description": "A well-stocked pantry with a variety of snacks and drinks.",
        "items": ["snacks", "drinks"]
    },
    "garage": {
        "name": "Garage",
        "north": "bathroom",
        "south": "dining_room",
        "east": "pantry",
        "west": "office",
        "description": "A spacious garage with a workshop and storage space.",
        "items": []
    },
    "closet": {
        "name": "Closet",
        "north": "bedroom",
        "south": "office",
        "east": "balcony",
        "west": "pantry",
        "description": "A spacious closet with a variety of clothes and accessories.",
        "items": ["clothes", "accessories"]
    },
    "office": {
        "name": "Office",
        "north": "bedroom",
        "south": "garage",
        "east": "balcony",
        "west": "closet",
        "description": "A spacious office with a desk and comfortable chair.",
        "items": ["chair", "desk"]
    },
    "balcony": {
        "name": "Balcony",
        "north": "living_room",
        "south": "pantry",
        "east": "office",
        "west": "closet",
        "description": "A spacious balcony with a view of the city.",
        "items": []
    }
}