from enum import Enum
import pygame

# Changed pygame_colors to common.GameColor enum. Has methods for converting human-friendly name to pygame hex code and
# vice versa. GameColor has mapping methods from name to hex and vice versa. Otherwise it would belong in
# resources\static.

class GameColor(Enum):
    # Yellows (Darkest to Lightest)
    GOLDENROD = (218, 165, 32)
    GOLD = (255, 215, 0)
    AMBER = (255, 193, 7)
    CYBER_YELLOW = (255, 211, 0)
    JONQUIL = (244, 202, 22)
    SUNGLOW = (255, 204, 51)
    DANDELION = (240, 225, 48)
    LEMON = (255, 247, 0)
    LIGHT_YELLOW = (255, 255, 224)
    IVORY = (255, 255, 240)

    # Oranges (Darkest to Lightest)
    BURNT_ORANGE = (204, 85, 0)
    RUST = (183, 65, 14)
    PUMPKIN = (255, 117, 24)
    DEEP_ORANGE = (255, 87, 34)
    ORANGE_RED = (255, 69, 0)
    DARK_ORANGE = (255, 140, 0)
    ORANGE = (255, 152, 0)
    CORAL = (255, 127, 80)
    TANGERINE = (242, 133, 0)
    PEACH = (255, 229, 180)

    # Reds (Darkest to Lightest)
    BURGUNDY = (128, 0, 32)
    FIREBRICK = (178, 34, 34)
    CARMINE = (150, 0, 24)
    CRIMSON = (220, 20, 60)
    TOMATO = (255, 99, 71)
    RED = (244, 67, 54)
    SCARLET = (255, 36, 0)
    VERMILION = (227, 66, 52)
    CORAL_RED = (255, 64, 64)
    CANDY_APPLE_RED = (255, 8, 0)
    ROSE_RED = (194, 30, 86)

    # Salmons (Darkest to Lightest)
    SALMON = (250, 128, 114)
    LIGHT_SALMON = (255, 160, 122)
    SALMON_PINK = (255, 145, 164)
    LIGHT_SALMON_PINK = (231, 206, 213)
    MISTY_ROSE = (255, 228, 225)

    # Primary Colors
    PINK = (233, 30, 99)

    # Purples (Darkest to Lightest)
    DARK_VIOLET = (148, 0, 211)
    INDIGO_PURPLE = (75, 0, 130)
    DARK_ORCHID = (153, 50, 204)
    PURPLE = (128, 0, 128)
    DEEP_PURPLE = (103, 58, 183)
    REBECCA_PURPLE = (102, 51, 153)
    MEDIUM_ORCHID = (186, 85, 211)
    AMETHYST = (153, 102, 204)
    ORCHID = (218, 112, 214)
    THISTLE = (216, 191, 216)
    LAVENDER = (230, 230, 250)
    INDIGO = (63, 81, 181)

    # Blues (Darkest to Lightest)
    BLUE_GRAY = (96, 125, 139)
    BATTLESHIP_GRAY_BLUE = (43, 60, 65, 225)  # RGBA
    NAVY_BLUE = (0, 31, 63)
    MIDNIGHT_BLUE = (25, 25, 112)
    ROYAL_BLUE = (65, 105, 225)
    BLUE = (33, 150, 243)
    DODGER_BLUE = (30, 144, 255)
    CERULEAN = (0, 123, 167)
    SKY_BLUE = (135, 206, 235)
    LIGHT_SKY_BLUE = (135, 206, 250)
    LIGHT_BLUE = (3, 169, 244)
    POWDER_BLUE = (176, 224, 230)
    POWDER_BLUE_GRAY = (152, 180, 185)

    # Cyan/Teal
    CYAN = (0, 188, 212)
    TEAL = (0, 150, 136)

    # Greens (Darkest to Lightest)
    GREEN_DARKEST = (1, 50, 32)
    FOREST_GREEN = (34, 139, 34)
    SEA_GREEN = (46, 139, 87)
    OLIVE_DRAB = (85, 107, 47)
    OLIVE_GREEN = (107, 142, 35)
    MEDIUM_GREEN = (60, 179, 113)
    GREEN = (76, 175, 80)
    LIGHT_GREEN = (139, 195, 74)
    PALE_GREEN = (152, 251, 152)
    MINT_GREEN = (245, 255, 250)
    LIME = (205, 220, 57)

    # Earth Tones
    BROWN = (121, 85, 72)
    MAROON = (128, 0, 0)
    OLIVE = (61, 153, 112)

    # Sand/Khaki Shades (Darkest to Lightest)
    SAND_DARKEST = (119, 94, 63)
    SAND_DARKER = (158, 123, 79)
    SAND_DARK = (194, 178, 128)
    SAND = (238, 214, 163)
    SAND_LIGHT = (245, 222, 179)
    SAND_LIGHTER = (255, 248, 225)
    SAND_LIGHTEST = (243, 236, 227)
    PALE_SAND = (216, 206, 201)

    # Greyscale (Darkest to Lightest)
    BLACK = (0, 0, 0)
    DARK_GRAY_1 = (28, 28, 28)
    DARK_GRAY_2 = (56, 56, 56)
    GRAY_1 = (85, 85, 85)
    GRAY_2 = (119, 119, 119)
    GRAY_3 = (153, 153, 153)
    GRAY = (158, 158, 158)
    LIGHT_GRAY_1 = (187, 187, 187)
    LIGHT_GRAY_2 = (220, 220, 220)
    LIGHT_GRAY_3 = (239, 239, 239)
    SILVER = (221, 221, 221)
    WHITE = (255, 255, 255)
    TRANSPARENT = (0, 0, 0, 0)

    @property
    def pygame_color(self) -> pygame.Color:
        """Convert to pygame.Color for rendering"""
        if len(self.value) == 4:  # RGBA
            return pygame.Color(*self.value)
        else:  # RGB
            return pygame.Color(*self.value)

    @classmethod
    def from_pygame_color(cls, pygame_color: pygame.Color) -> 'GameColor':
        """Find GameColor from pygame.Color"""
        # Handle alpha channel
        if pygame_color.a != 255:
            target_rgba = (pygame_color.r, pygame_color.g, pygame_color.b, pygame_color.a)
            for color in cls:
                if len(color.value) == 4 and color.value == target_rgba:
                    return color

        # Handle RGB only
        target_rgb = (pygame_color.r, pygame_color.g, pygame_color.b)
        for color in cls:
            if len(color.value) == 3 and color.value == target_rgb:
                return color
            elif len(color.value) == 4 and color.value[:3] == target_rgb:
                return color

        raise ValueError(
            f"No GameColor found for pygame.Color({pygame_color.r}, {pygame_color.g}, {pygame_color.b}, {pygame_color.a})")

    @classmethod
    def by_name(cls, name: str) -> 'GameColor':
        """Get color by string name (case insensitive)"""
        try:
            return cls[name.upper()]
        except KeyError:
            raise ValueError(f"No GameColor found with name '{name}'")


# Convenience constants for defaults
DEFAULT_BOX_COLOR = GameColor.POWDER_BLUE
DEFAULT_ICON_BACKGROUND_COLOR = GameColor.LAVENDER
DEFAULT_DISPLAY_BACKGROUND_COLOR = GameColor.POWDER_BLUE_GRAY
DEFAULT_HEADING_COLOR = GameColor.PALE_SAND