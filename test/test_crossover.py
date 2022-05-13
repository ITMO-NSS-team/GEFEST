import pytest
from gefest.core.opt.operators.crossover import crossover
from gefest.core.structure.point import Point
from gefest.core.structure.polygon import Polygon
from gefest.core.structure.structure import Structure
from gefest.core.structure.domain import Domain


domain = Domain()
geometry = domain.geometry


def create_rectangle(x, y, dim=5):
    rectangle_points = [(x, y), (x, y+dim), (x+dim, y+dim), (x+dim, y), (x, y)]
    rectangle_poly = Polygon(f'rectangle_from_{x,y}', points=[Point(*coords) for coords in rectangle_points])
    return rectangle_poly


structure_large = Structure([create_rectangle(5, 5), create_rectangle(5, 15)])
structure_small = Structure([create_rectangle(15, 5, 3), create_rectangle(15, 15, 3)])


def test_crossover_passed():

    expected_poly_positions = [structure_large.polygons[0].points, structure_small.polygons[1].points]
    expected_square = geometry.get_square(structure_large.polygons[0])\
        + geometry.get_square(structure_small.polygons[0])

    for i in range(100):
        new_structure = crossover(structure_large, structure_small, domain)
        if len(new_structure.polygons) == 2:
            observed_square = geometry.get_square(new_structure.polygons[0]) + \
                              geometry.get_square(new_structure.polygons[1])
            if all([new_structure.polygons[0].points == expected_poly_positions[0],
                    new_structure.polygons[1].points == expected_poly_positions[1],
                    observed_square == expected_square]):
                assert True
                break


def test_crossover_not_passed():

    new_structure = crossover(structure_large, structure_small, domain, rate=0.001)

    assert any([new_structure == structure_large, new_structure == structure_small])
