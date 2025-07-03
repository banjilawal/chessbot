import random
from enum import global_enum_repr

from common.dimension import Dimension
from common.id_generator import IdGenerator, global_id_generator
from model.occupant.boulder import Boulder
from model.occupant.crate import Crate


def random_dimension():
    return Dimension(
        length=random.randint(1, 6),
        height=random.randint(1, 6)
    )

def generate_boulder():
    boulder = Boulder(id=global_id_generator.next_boulder_id(), dimension=random_dimension())
    print("created boulder with id:", boulder.id, "and dimension:", boulder.dimension, "area:", boulder.dimension.area())
    return boulder

def generate_boulders(count: int):
    boulders = []
    for _ in range(count):
        boulder = generate_boulder()
        boulders.append(boulder)
    return boulders

def generate_crate():
    crate = Crate(id=global_id_generator.next_crate_id(), dimension=random_dimension())
    print("created crate with id:", crate.id, "and dimension:", crate.dimension, "area:", crate.dimension.area())

def generate_crates(count: int):
    crates = []
    for _ in range(count):
        crate = generate_crate()
        crates.append(crate)
    return crates

if __name__ == "__main__":
    generate_boulders(10)
    generate_crates(12)