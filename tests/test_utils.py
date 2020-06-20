import unittest

from universe import components, engine, utils


class PlanetProductionTestCase(unittest.TestCase):
    def test_values(self):
        manager = engine.Manager()
        manager.register_entity_type('species', [
            components.SpeciesProductionComponent(),
        ])
        manager.register_entity_type('planet', [
            components.PopulationComponent(),
        ])
        engine.Entity.register_manager(manager)

        data = [
            (700, 0, 0),
            (700, 699, 0),
            (700, 700, 1),
            (700, 1_000_000, 1428),
            (1000, 0, 0),
            (1000, 999, 0),
            (1000, 1000, 1),
            (1000, 1_000_000, 1000),
            (1500, 0, 0),
            (1500, 1499, 0),
            (1500, 1500, 1),
            (1500, 1_000_000, 666),
        ]

        for per, pop, value in data:
            species = engine.Entity(**{
                'type': 'species',
                'population_per_r': per,
                'minerals_per_m': 5,
                'mines_cost_r': 2,
                'mines_per_pop': 5,
            })
            planet = engine.Entity(**{
                'type': 'planet',
                'population': pop,
            })
            self.assertEqual(utils.production(species, planet), value,
                             f"population_per_r: {per}, population: {pop}")


class PlanetValueTestCase(unittest.TestCase):
    def test_values(self):
        manager = engine.Manager()
        manager.register_entity_type('species', [
            components.SpeciesComponent(),
        ])
        manager.register_entity_type('planet', [
            components.EnvironmentComponent(),
        ])
        engine.Entity.register_manager(manager)

        species = engine.Entity(**
            {'type': 'species',
             'name': 'Human',
             'plural_name': 'Humans',
             'growth_rate': 15,
             'gravity_immune': False,
             'gravity_min': 32,
             'gravity_max': 86,
             'temperature_immune': False,
             'temperature_min': 10,
             'temperature_max': 64,
             'radiation_immune': False,
             'radiation_min': 38,
             'radiation_max': 90,}
        )

        data = [  # Taken from a historical Stars game.
            (59, 37, 64, 100),
            (59, 36, 64, 99),
            (57, 37, 64, 98),
            (59, 37, 66, 98),
            (59, 35, 64, 98),
            (62, 37, 64, 97),
            (59, 35, 63, 97),
            (59, 37, 61, 97),
            (59, 40, 64, 97),
            (59, 39, 66, 96),
            (59, 33, 64, 96),
            (59, 36, 68, 95),
            (59, 33, 63, 95),
            (59, 41, 66, 94),
            (53, 37, 64, 94),
            (59, 31, 64, 94),
            (62, 37, 61, 93),
            (59, 44, 64, 93),
            (59, 37, 57, 93),
            (59, 31, 63, 93),
            (59, 45, 64, 92),
            (67, 37, 64, 92),
            (59, 36, 70, 92),
            (59, 37, 72, 92),
            (61, 32, 64, 92),
            (59, 29, 63, 91),
            (59, 47, 64, 90),
            (59, 45, 66, 89),
            (66, 37, 61, 89),
            (69, 36, 64, 89),
            (67, 37, 62, 89),
            (59, 37, 53, 89),
            (59, 37, 76, 88),
            (59, 36, 75, 88),
            (60, 27, 63, 88),
            (59, 26, 65, 88),
            (61, 28, 64, 88),
            (47, 38, 64, 87),
            (59, 36, 76, 87),
            (59, 38, 51, 86),
            (71, 37, 62, 86),
            (68, 41, 64, 86),
            (70, 35, 65, 85),
            (45, 37, 64, 85),
            (73, 37, 64, 85),
            (59, 51, 64, 85),
            (59, 45, 70, 84),
            (52, 40, 68, 84),
            (61, 24, 63, 84),
            (71, 37, 60, 83),
            (63, 26, 65, 83),
            (60, 27, 60, 83),
            (52, 41, 68, 83),
            (68, 35, 68, 83),
            (61, 30, 58, 82),
            (46, 42, 64, 81),
            (56, 51, 64, 81),
            (60, 27, 58, 81),
            (73, 34, 64, 81),
            (52, 42, 68, 81),
            (68, 45, 64, 81),
            (73, 37, 61, 81),
            (51, 35, 57, 80),
            (53, 35, 55, 80),
            (72, 31, 64, 80),
            (60, 27, 57, 80),
            (68, 33, 68, 80),
            (59, 42, 51, 80),
            (59, 32, 77, 80),
            (66, 26, 65, 79),
            (51, 35, 56, 79),
            (59, 37, 49, 79),
            (59, 51, 60, 79),
            (73, 37, 60, 79),
            (68, 32, 68, 79),
            (59, 30, 77, 78),
            (72, 37, 57, 78),
            (61, 27, 57, 78),
            (59, 51, 59, 78),
            (52, 43, 69, 78),
            (60, 24, 70, 78),
            (59, 24, 71, 78),
            (61, 26, 58, 78),
            (57, 42, 77, 78),
            (52, 43, 70, 77),
            (60, 24, 71, 77),
            (73, 43, 64, 77),
            (62, 27, 57, 76),
            (58, 48, 73, 76),
            (59, 46, 51, 76),
            (73, 31, 65, 76),
            (72, 37, 55, 76),
            (60, 24, 72, 76),
            (61, 24, 70, 76),
            (59, 37, 48, 75),
            (52, 43, 72, 75),
            (68, 33, 56, 75),
            (68, 29, 68, 75),
            (73, 45, 64, 75),
            (60, 24, 73, 74),
            (52, 43, 73, 74),
            (59, 26, 77, 74),
            (68, 46, 68, 74),
            (61, 24, 56, 74),
            (46, 43, 68, 73),
            (68, 27, 68, 73),
            (68, 33, 74, 73),
            (63, 24, 70, 73),
            (71, 50, 64, 73),
            (72, 37, 51, 72),
            (52, 43, 74, 72),
            (68, 26, 68, 72),
            (73, 47, 64, 72),
            (73, 36, 54, 71),
            (62, 46, 51, 71),
            (52, 43, 75, 71),
            (51, 50, 68, 71),
            (43, 42, 64, 71),
            (55, 34, 49, 70),
            (59, 54, 61, 70),
            (68, 50, 68, 70),
            (65, 24, 70, 70),
            (66, 46, 74, 69),
            (41, 37, 64, 69),
            (73, 50, 64, 69),
            (52, 48, 73, 68),
            (75, 31, 65, 68),
            (67, 24, 70, 68),
            (68, 24, 69, 68),
            (56, 49, 77, 68),
            (68, 27, 72, 67),
            (43, 46, 64, 67),
            (63, 26, 51, 67),
            (74, 28, 61, 66),
            (65, 46, 51, 66),
            (68, 33, 78, 66),
            (73, 34, 53, 66),
            (41, 36, 61, 65),
            (47, 42, 77, 65),
            (51, 43, 78, 64),
            (59, 37, 45, 64),
            (73, 34, 51, 64),
            (43, 49, 64, 64),
            (64, 38, 81, 64),
            (73, 51, 66, 64),
            (53, 55, 64, 63),
            (49, 27, 54, 63),
            (50, 43, 78, 63),
            (59, 56, 61, 63),
            (57, 23, 78, 63),
            (73, 32, 53, 63),
            (66, 26, 51, 63),
            (57, 25, 79, 62),
            (59, 55, 71, 62),
            (69, 40, 79, 62),
            (75, 28, 61, 62),
            (77, 31, 65, 62),
            (65, 24, 51, 62),
            (53, 50, 77, 62),
            (60, 32, 46, 61),
            (73, 32, 51, 61),
            (56, 23, 78, 61),
            (47, 42, 78, 61),
            (41, 37, 56, 61),
            (47, 45, 77, 60),
            (68, 26, 51, 60),
            (76, 28, 61, 59),
            (66, 46, 49, 59),
            (41, 37, 74, 59),
            (56, 22, 78, 58),
            (74, 31, 53, 58),
            (62, 32, 46, 58),
            (43, 52, 64, 58),
            (64, 38, 45, 57),
            (59, 58, 61, 57),
            (64, 38, 83, 57),
            (73, 51, 58, 57),
            (78, 33, 68, 57),
            (70, 26, 51, 57),
            (41, 37, 52, 57),
            (77, 28, 61, 56),
            (74, 31, 51, 56),
            (79, 31, 65, 56),
            (69, 24, 51, 56),
            (73, 53, 67, 56),
            (49, 50, 77, 56),
            (66, 46, 48, 55),
            (67, 38, 45, 55),
            (72, 26, 51, 55),
            (52, 51, 50, 55),
            (58, 35, 43, 54),
            (56, 21, 78, 54),
            (45, 46, 77, 54),
            (79, 33, 68, 54),
            (78, 28, 61, 53),
            (76, 31, 53, 53),
            (39, 37, 74, 53),
            (47, 50, 77, 53),
            (41, 39, 51, 53),
            (56, 20, 78, 52),
            (63, 16, 67, 52),
            (66, 46, 47, 52),
            (62, 32, 44, 52),
            (80, 31, 65, 52),
            (47, 37, 83, 52),
            (72, 24, 51, 52),
            (64, 38, 85, 51),
            (47, 42, 81, 51),
            (69, 57, 66, 50),
            (76, 31, 51, 50),
            (59, 60, 61, 50),
            (46, 51, 77, 50),
            (48, 51, 50, 50),
            (70, 42, 82, 50),
            (66, 46, 46, 49),
            (67, 40, 44, 49),
            (77, 31, 53, 49),
            (47, 37, 84, 49),
            (47, 39, 83, 49),
            (77, 31, 52, 49),
            (41, 42, 51, 49),
            (47, 40, 83, 48),
            (43, 46, 77, 48),
            (73, 56, 67, 48),
            (82, 31, 65, 47),
            (47, 35, 84, 47),
            (37, 37, 74, 47),
            (81, 42, 68, 47),
            (48, 56, 70, 46),
            (65, 32, 43, 46),
            (62, 32, 42, 46),
            (47, 42, 83, 46),
            (78, 31, 52, 46),
            (72, 22, 51, 46),
            (82, 33, 68, 46),
            (64, 38, 87, 45),
            (78, 31, 51, 45),
            (73, 42, 82, 45),
            (59, 62, 61, 44),
            (79, 31, 53, 44),
            (43, 57, 64, 44),
            (47, 35, 85, 44),
            (84, 33, 64, 44),
            (72, 23, 49, 44),
            (41, 45, 51, 44),
            (70, 27, 82, 43),
            (75, 28, 79, 43),
            (75, 56, 67, 43),
            (46, 52, 78, 43),
            (68, 59, 69, 42),
            (66, 32, 42, 42),
            (35, 37, 74, 42),
            (84, 32, 63, 42),
            (84, 33, 66, 42),
            (47, 51, 48, 42),
            (84, 31, 65, 41),
            (80, 31, 53, 41),
            (47, 35, 86, 41),
            (67, 40, 41, 40),
            (81, 31, 53, 39),
            (41, 45, 49, 39),
            (47, 35, 87, 38),
            (40, 57, 64, 38),
            (85, 32, 62, 38),
            (77, 56, 67, 38),
            (46, 53, 79, 38),
            (77, 42, 82, 37),
            (77, 54, 57, 37),
            (85, 30, 62, 37),
            (33, 37, 74, 36),
            (48, 35, 88, 36),
            (85, 29, 62, 36),
            (72, 21, 48, 36),
            (40, 45, 48, 35),
            (32, 37, 74, 34),
            (83, 31, 53, 34),
            (59, 23, 89, 34),
            (59, 17, 44, 34),
            (62, 19, 44, 34),
            (79, 56, 67, 34),
            (47, 51, 45, 34),
            (67, 40, 38, 33),
            (72, 19, 49, 33),
            (38, 57, 64, 33),
            (61, 18, 44, 33),
            (75, 28, 83, 33),
            (46, 54, 80, 33),
            (84, 31, 53, 32),
            (78, 42, 83, 32),
            (66, 32, 38, 32),
            (57, 17, 44, 32),
            (62, 19, 43, 32),
            (83, 38, 48, 32),
            (71, 11, 68, 31),
            (56, 17, 44, 31),
            (72, 18, 49, 31),
            (37, 57, 64, 31),
            (41, 57, 57, 31),
            (72, 20, 47, 31),
            (38, 45, 48, 31),
            (83, 35, 48, 31),
            (69, 16, 49, 30),
            (81, 56, 67, 30),
            (83, 40, 48, 30),
            (72, 17, 49, 29),
            (79, 56, 57, 29),
            (65, 19, 43, 29),
            (32, 50, 68, 29),
            (46, 54, 82, 29),
            (37, 45, 48, 29),
            (84, 31, 78, 29),
            (83, 33, 48, 29),
            (67, 20, 43, 28),
            (68, 17, 82, 28),
            (47, 53, 44, 28),
            (49, 12, 52, 28),
            (35, 57, 64, 27),
            (69, 45, 38, 27),
            (32, 51, 68, 27),
            (41, 59, 57, 27),
            (38, 56, 57, 27),
            (37, 55, 57, 27),
            (36, 45, 48, 27),
            (84, 31, 79, 27),
            (71, 17, 47, 26),
            (34, 57, 64, 26),
            (86, 51, 70, 26),
            (32, 51, 70, 26),
            (41, 59, 56, 26),
            (61, 12, 46, 26),
            (72, 19, 46, 26),
            (68, 17, 83, 26),
            (47, 12, 52, 26),
            (48, 12, 52, 26),
            (84, 56, 67, 25),
            (83, 47, 49, 25),
            (46, 54, 84, 25),
            (72, 17, 47, 25),
            (35, 45, 48, 25),
            (46, 12, 52, 25),
            (33, 57, 64, 24),
            (86, 52, 70, 24),
            (73, 20, 44, 24),
            (59, 10, 46, 24),
            (41, 59, 54, 24),
            (61, 11, 46, 24),
            (84, 28, 79, 24),
            (47, 55, 44, 24),
            (45, 12, 52, 24),
            (46, 54, 85, 23),
            (86, 53, 70, 23),
            (73, 17, 47, 23),
            (45, 63, 53, 23),
            (61, 10, 46, 23),
            (67, 20, 40, 23),
            (72, 18, 45, 23),
            (34, 45, 48, 23),
            (84, 27, 79, 23),
            (70, 17, 83, 23),
            (32, 57, 64, 22),
            (83, 42, 84, 22),
            (44, 12, 52, 22),
            (65, 17, 41, 22),
            (32, 51, 74, 22),
            (73, 19, 44, 22),
            (33, 45, 48, 22),
            (76, 15, 78, 21),
            (84, 54, 74, 21),
            (84, 25, 79, 21),
            (47, 55, 42, 21),
            (72, 16, 83, 20),
            (41, 61, 53, 20),
            (32, 45, 48, 20),
            (72, 17, 44, 20),
            (73, 17, 83, 20),
            (36, 23, 81, 19),
            (49, 12, 46, 19),
            (42, 63, 53, 18),
            (73, 19, 41, 18),
            (72, 16, 44, 18),
            (86, 25, 79, 18),
            (47, 57, 42, 18),
            (48, 12, 46, 18),
            (86, 58, 69, 17),
            (72, 16, 43, 17),
            (47, 58, 42, 17),
            (47, 12, 46, 17),
            (72, 15, 43, 16),
            (71, 60, 85, 16),
            (73, 20, 39, 16),
            (73, 19, 40, 16),
            (75, 17, 83, 16),
            (47, 59, 42, 16),
            (32, 29, 84, 16),
            (46, 12, 46, 16),
            (85, 60, 71, 15),
            (83, 46, 41, 15),
            (45, 12, 46, 15),
            (76, 16, 83, 14),
            (47, 60, 42, 14),
            (44, 12, 46, 14),
            (47, 61, 42, 13),
            (47, 62, 41, 12),
            (47, 61, 41, 12),
            (43, 12, 46, 12),
            (32, 64, 68, 12),
            (42, 12, 46, 11),
            (77, 14, 83, 11),
            (86, 57, 49, 10),
            (70, 63, 38, 9),
            (77, 12, 83, 9),
            (34, 23, 90, 8),
            (77, 10, 83, 8),
            (75, 12, 88, 7),
            (34, 10, 79, 6),
            (39, 13, 42, 5),
            (32, 60, 85, 3),
            (32, 59, 85, 3),
            (32, 63, 85, 2),
            (75, 9, 88, -1),
            (47, 41, 37, -1),
            (87, 20, 51, -1),
            (87, 53, 70, -1),
            (83, 65, 60, -1),
            (45, 65, 53, -1),
            (31, 45, 48, -1),
            (32, 65, 85, -1),
            (87, 25, 79, -1),
            (49, 41, 37, -1),
            (50, 41, 37, -1),
            (73, 45, 37, -1),
            (31, 29, 84, -1),
            (51, 41, 37, -1),
            (52, 41, 37, -1),
            (76, 53, 36, -2),
            (88, 34, 73, -2),
            (75, 63, 36, -2),
            (30, 45, 48, -2),
            (88, 53, 70, -2),
            (48, 66, 48, -2),
            (48, 66, 50, -2),
            (54, 8, 46, -2),
            (48, 66, 51, -2),
            (55, 8, 46, -2),
            (47, 66, 53, -2),
            (57, 8, 46, -2),
            (59, 8, 46, -2),
            (67, 20, 36, -2),
            (77, 8, 83, -2),
            (72, 8, 44, -2),
            (89, 29, 62, -3),
            (89, 57, 49, -3),
            (77, 7, 83, -3),
            (89, 18, 53, -3),
            (50, 7, 46, -3),
            (84, 20, 35, -3),
            (48, 44, 35, -3),
            (52, 7, 46, -3),
            (89, 53, 70, -3),
            (53, 7, 46, -3),
            (67, 20, 35, -3),
            (31, 66, 85, -3),
            (89, 25, 79, -3),
            (73, 19, 35, -3),
            (51, 44, 35, -3),
            (53, 44, 35, -3),
            (51, 65, 36, -3),
            (54, 44, 35, -3),
            (58, 44, 35, -3),
            (59, 44, 35, -3),
            (89, 31, 78, -3),
            (46, 7, 90, -3),
            (46, 7, 89, -3),
            (63, 23, 34, -4),
            (90, 18, 76, -4),
            (30, 15, 36, -4),
            (56, 68, 70, -4),
            (90, 53, 70, -4),
            (44, 32, 94, -4),
            (66, 32, 34, -4),
            (73, 20, 34, -4),
            (30, 66, 85, -4),
            (90, 25, 79, -4),
            (67, 20, 34, -4),
            (72, 6, 38, -4),
            (51, 65, 35, -4),
            (72, 6, 42, -4),
            (59, 44, 34, -4),
            (28, 29, 84, -4),
            (83, 46, 34, -4),
            (46, 7, 91, -4),
            (70, 32, 34, -4),
            (36, 69, 54, -5),
            (66, 59, 33, -5),
            (91, 61, 52, -5),
            (36, 69, 77, -5),
            (27, 58, 48, -5),
            (66, 69, 78, -5),
            (91, 53, 70, -5),
            (63, 10, 95, -5),
            (27, 27, 69, -5),
            (27, 25, 90, -5),
            (27, 25, 89, -5),
            (91, 25, 79, -5),
            (27, 25, 88, -5),
            (27, 25, 86, -5),
            (27, 25, 85, -5),
            (27, 25, 84, -5),
            (51, 65, 34, -5),
            (27, 26, 84, -5),
            (27, 27, 84, -5),
            (27, 29, 84, -5),
            (59, 44, 33, -5),
            (46, 7, 92, -5),
            (91, 38, 47, -5),
            (32, 21, 32, -6),
            (67, 70, 64, -6),
            (73, 32, 32, -6),
            (92, 53, 70, -6),
            (86, 33, 32, -6),
            (36, 14, 96, -6),
            (26, 52, 88, -6),
            (67, 25, 96, -6),
            (83, 69, 37, -6),
            (92, 25, 79, -6),
            (30, 68, 85, -6),
            (73, 23, 32, -6),
            (73, 25, 32, -6),
            (73, 28, 32, -6),
            (85, 33, 32, -6),
            (83, 32, 32, -6),
            (46, 7, 93, -6),
            (92, 38, 38, -6),
            (92, 38, 40, -6),
            (92, 38, 41, -6),
            (92, 38, 43, -6),
            (26, 52, 87, -6),
            (92, 38, 45, -6),
            (26, 52, 85, -6),
            (92, 38, 46, -6),
            (26, 52, 84, -6),
            (39, 71, 72, -7),
            (28, 12, 35, -7),
            (73, 32, 31, -7),
            (64, 71, 56, -7),
            (75, 27, 31, -7),
            (73, 25, 31, -7),
            (25, 26, 85, -7),
            (73, 30, 31, -7),
            (75, 31, 31, -7),
            (25, 44, 55, -7),
            (53, 62, 97, -7),
            (73, 45, 31, -7),
            (77, 24, 31, -7),
            (27, 25, 92, -7),
            (93, 25, 79, -7),
            (84, 32, 31, -7),
            (30, 69, 85, -7),
            (67, 22, 31, -7),
            (67, 26, 31, -7),
            (62, 32, 31, -7),
            (66, 32, 31, -7),
            (73, 28, 31, -7),
            (93, 37, 61, -7),
            (73, 27, 31, -7),
            (46, 7, 94, -7),
            (59, 40, 31, -7),
            (78, 32, 31, -7),
            (59, 39, 31, -7),
            (75, 32, 31, -7),
            (73, 42, 31, -7),
            (80, 32, 31, -7),
            (73, 31, 31, -7),
            (70, 32, 31, -7),
            (73, 41, 31, -7),
            (63, 32, 31, -7),
            (67, 32, 31, -7),
            (78, 72, 71, -8),
            (72, 20, 30, -8),
            (42, 66, 96, -8),
            (77, 28, 98, -8),
            (39, 65, 31, -8),
            (30, 51, 32, -8),
            (39, 22, 98, -8),
            (84, 32, 30, -8),
            (72, 6, 34, -8),
            (86, 58, 98, -8),
            (71, 7, 33, -8),
            (24, 10, 87, -8),
            (88, 70, 69, -8),
            (80, 29, 98, -8),
            (30, 70, 90, -8),
            (27, 25, 93, -8),
            (30, 70, 88, -8),
            (30, 70, 87, -8),
            (30, 70, 85, -8),
            (92, 38, 36, -8),
            (75, 41, 30, -8),
            (73, 20, 30, -8),
            (24, 50, 86, -8),
            (46, 7, 95, -8),
            (73, 41, 30, -8),
            (73, 37, 30, -8),
            (67, 25, 99, -9),
            (36, 52, 99, -9),
            (23, 61, 65, -9),
            (74, 32, 99, -9),
            (68, 30, 99, -9),
            (32, 39, 99, -9),
            (58, 73, 70, -9),
            (95, 25, 79, -9),
            (78, 73, 88, -9),
            (62, 12, 29, -9),
            (93, 44, 36, -9),
            (32, 37, 29, -9),
            (30, 70, 91, -9),
            (27, 25, 94, -9),
            (92, 38, 35, -9),
            (23, 50, 86, -9),
            (23, 50, 50, -9),
            (46, 7, 96, -9),
            (81, 73, 91, -10),
            (27, 20, 95, -10),
            (22, 49, 82, -10),
            (27, 21, 95, -10),
            (84, 32, 28, -10),
            (27, 23, 95, -10),
            (30, 70, 92, -10),
            (27, 24, 95, -10),
            (92, 38, 34, -10),
            (23, 65, 68, -10),
            (22, 50, 50, -10),
            (28, 32, 31, -11),
            (92, 15, 33, -11),
            (92, 38, 33, -11),
            (84, 32, 27, -11),
            (30, 70, 93, -11),
            (62, 32, 27, -11),
            (82, 76, 75, -12),
            (93, 44, 33, -12),
            (84, 76, 62, -12),
            (65, 74, 92, -12),
            (88, 10, 28, -12),
            (73, 33, 26, -12),
            (88, 13, 28, -12),
            (75, 41, 26, -12),
            (30, 70, 94, -12),
            (93, 25, 95, -12),
            (20, 50, 86, -12),
            (69, 36, 25, -13),
            (78, 56, 25, -13),
            (98, 9, 90, -13),
            (19, 21, 39, -13),
            (84, 32, 25, -13),
            (51, 65, 26, -13),
            (47, 72, 95, -13),
            (46, 60, 25, -13),
            (19, 21, 61, -13),
            (46, 6, 99, -13),
            (19, 49, 46, -13),
            (19, 49, 49, -13),
            (19, 49, 50, -13),
            (19, 50, 50, -13),
            (19, 50, 45, -13),
            (30, 70, 96, -14),
            (37, 66, 26, -14),
            (18, 53, 63, -14),
            (55, 70, 30, -14),
            (18, 49, 46, -14),
            (18, 50, 86, -14),
            (62, 32, 24, -14),
            (65, 32, 24, -14),
            (73, 20, 24, -14),
            (69, 32, 24, -14),
            (14, 28, 85, -15),
            (84, 33, 22, -15),
            (78, 63, 15, -15),
            (74, 61, 12, -15),
            (54, 34, 9, -15),
            (72, 49, 13, -15),
            (52, 44, 16, -15),
            (10, 37, 56, -15),
            (80, 54, 20, -15),
            (17, 14, 89, -15),
            (67, 90, 66, -15),
            (57, 62, 7, -15),
            (85, 16, 19, -15),
            (9, 17, 66, -15),
            (55, 34, 22, -15),
            (58, 91, 89, -15),
            (86, 52, 15, -15),
            (66, 56, 6, -15),
            (57, 90, 89, -15),
            (46, 19, 2, -15),
            (13, 27, 90, -15),
            (70, 87, 65, -15),
            (41, 33, 7, -15),
            (59, 45, 6, -15),
            (84, 32, 23, -15),
            (35, 89, 65, -15),
            (61, 54, 12, -15),
            (26, 37, 99, -15),
            (72, 91, 56, -15),
            (82, 45, 18, -15),
            (11, 30, 85, -15),
            (52, 92, 63, -15),
            (15, 61, 46, -15),
            (69, 16, 17, -15),
            (79, 17, 22, -15),
            (45, 20, 22, -15),
            (85, 39, 17, -15),
            (84, 36, 18, -15),
            (63, 17, 4, -15),
            (6, 31, 61, -15),
            (80, 50, 20, -15),
            (80, 44, 20, -15),
            (58, 80, 44, -15),
            (22, 69, 44, -15),
            (79, 44, 20, -15),
            (51, 49, 14, -15),
            (53, 79, 62, -15),
            (34, 89, 89, -15),
            (10, 51, 72, -15),
            (35, 88, 85, -15),
            (43, 47, 8, -15),
            (23, 70, 68, -15),
            (35, 90, 56, -15),
            (38, 79, 61, -15),
            (17, 11, 69, -15),
            (74, 50, 1, -15),
            (79, 63, 5, -15),
            (78, 44, 20, -15),
            (77, 27, 21, -15),
            (69, 41, 6, -15),
            (15, 55, 90, -15),
            (59, 90, 46, -15),
            (17, 47, 46, -15),
            (17, 35, 76, -15),
            (39, 88, 51, -15),
            (6, 64, 66, -15),
            (47, 79, 87, -15),
            (11, 39, 38, -15),
            (79, 80, 82, -15),
            (59, 21, 23, -15),
            (12, 33, 60, -15),
            (12, 32, 71, -15),
            (9, 35, 43, -15),
            (40, 94, 76, -15),
            (58, 82, 88, -15),
            (7, 54, 48, -15),
            (16, 55, 90, -15),
            (15, 61, 45, -15),
            (82, 90, 86, -15),
            (16, 53, 90, -15),
            (60, 35, 9, -15),
            (16, 51, 90, -15),
            (23, 55, 96, -15),
            (34, 88, 89, -15),
            (61, 34, 18, -15),
            (59, 45, 7, -15),
            (17, 50, 90, -15),
            (59, 45, 12, -15),
            (17, 50, 88, -15),
            (59, 45, 17, -15),
            (17, 50, 87, -15),
            (62, 44, 18, -15),
            (58, 34, 22, -15),
            (60, 34, 22, -15),
            (63, 32, 19, -15),
            (64, 44, 19, -15),
            (70, 16, 17, -15),
            (62, 33, 22, -15),
            (65, 44, 19, -15),
            (73, 19, 17, -15),
            (53, 44, 16, -15),
            (11, 39, 39, -15),
            (65, 32, 21, -15),
            (70, 43, 19, -15),
            (73, 19, 19, -15),
            (54, 44, 16, -15),
            (11, 39, 40, -15),
            (65, 32, 22, -15),
            (70, 38, 21, -15),
            (73, 20, 23, -15),
            (61, 44, 16, -15),
            (7, 64, 66, -15),
            (11, 39, 41, -15),
            (70, 34, 21, -15),
            (62, 44, 16, -15),
            (11, 39, 43, -15),
            (24, 3, 81, -15),
            (8, 64, 66, -15),
            (11, 39, 44, -15),
            (10, 64, 66, -15),
            (11, 64, 66, -15),
            (63, 44, 18, -15),
            (13, 64, 66, -15),
            (63, 44, 19, -15),
            (16, 64, 66, -15),
            (63, 43, 19, -15),
            (37, 79, 54, -15),
            (17, 64, 68, -15),
            (17, 35, 75, -15),
            (17, 61, 68, -15),
            (86, 48, 13, -15),
            (12, 39, 45, -15),
            (63, 37, 19, -15),
            (17, 57, 68, -15),
            (86, 48, 14, -15),
            (14, 39, 45, -15),
            (73, 34, 21, -15),
            (63, 34, 19, -15),
            (17, 54, 68, -15),
            (16, 40, 45, -15),
            (73, 32, 21, -15),
            (65, 32, 23, -15),
            (17, 53, 68, -15),
            (16, 44, 45, -15),
            (86, 48, 16, -15),
            (16, 47, 45, -15),
            (16, 50, 45, -15),
            (24, 2, 78, -16),
            (27, 75, 63, -16),
            (84, 89, 37, -16),
            (25, 66, 31, -16),
            (31, 88, 38, -16),
            (63, 92, 37, -16),
            (31, 92, 88, -16),
            (31, 93, 79, -16),
            (62, 95, 37, -16),
            (52, 9, 2, -16),
            (27, 26, 27, -16),
            (87, 49, 13, -16),
            (65, 75, 96, -17),
            (61, 79, 36, -17),
            (4, 20, 92, -17),
            (88, 23, 16, -17),
            (90, 77, 85, -17),
            (88, 73, 32, -17),
            (88, 51, 13, -17),
            (88, 50, 13, -17),
            (59, 67, 6, -18),
            (3, 14, 93, -18),
            (44, 7, 21, -18),
            (89, 51, 13, -18),
            (5, 36, 94, -19),
            (44, 91, 34, -19),
            (89, 78, 92, -19),
            (90, 51, 13, -19),
            (72, 74, 29, -19),
            (28, 21, 5, -19),
            (16, 23, 95, -20),
            (27, 13, 11, -20),
            (85, 75, 99, -20),
            (91, 39, 17, -20),
            (27, 81, 65, -20),
            (86, 70, 16, -21),
            (44, 78, 97, -21),
            (50, 96, 96, -21),
            (92, 28, 10, -21),
            (95, 76, 68, -21),
            (50, 70, 16, -21),
            (10, 4, 54, -21),
            (47, 71, 2, -22),
            (41, 89, 31, -22),
            (32, 85, 31, -22),
            (29, 72, 27, -22),
            (32, 84, 31, -22),
            (17, 3, 73, -22),
            (32, 83, 31, -22),
            (23, 14, 24, -23),
            (68, 83, 98, -23),
            (55, 95, 98, -23),
            (72, 87, 30, -23),
            (95, 39, 17, -24),
            (23, 11, 10, -24),
            (12, 42, 29, -24),
            (20, 3, 95, -24),
            (96, 16, 22, -25),
            (81, 74, 15, -25),
            (21, 90, 90, -26),
            (21, 20, 21, -26),
            (67, 76, 23, -27),
            (91, 93, 30, -28),
            (14, 77, 72, -28),
            (72, 82, 25, -28),
            (19, 84, 91, -29),
            (13, 74, 34, -29),
            (61, 86, 24, -29),
            (88, 76, 1, -29),
            (9, 27, 24, -29),
            (18, 61, 7, -29),
            (12, 64, 21, -30),
            (3, 85, 69, -30),
            (7, 79, 54, -30),
            (42, 90, 9, -30),
            (15, 79, 77, -30),
            (9, 92, 86, -30),
            (48, 85, 4, -30),
            (4, 89, 68, -30),
            (66, 85, 3, -30),
            (17, 94, 69, -30),
            (12, 34, 18, -30),
            (9, 47, 11, -30),
            (10, 42, 7, -30),
            (7, 85, 65, -30),
            (12, 19, 14, -30),
            (9, 94, 72, -30),
            (12, 80, 85, -30),
            (6, 82, 82, -30),
            (46, 86, 21, -30),
            (7, 22, 6, -30),
            (17, 24, 12, -30),
            (39, 87, 6, -30),
            (40, 84, 10, -30),
            (8, 74, 97, -32),
            (25, 81, 18, -37),
            (25, 93, 19, -37),
            (19, 78, 3, -42),
        ]

        for g, t, r, value in data:
            planet = engine.Entity(**
                {'type': 'planet',
                 'gravity': g,
                 'temperature': t,
                 'radiation': r}
            )
            self.assertEqual(utils.planet_value(species, planet), value)
