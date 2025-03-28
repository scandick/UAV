class NavigationSystem:
    """
    Включают GPS (Global Positioning System), инерциальные навигационные системы (INS), радионавигационные системы
    (например, VOR, ILS), которые обеспечивают точное позиционирование и навигацию.
    """
    def __init__(self):
        self.current_position = (0, 0)

    def update_position(self, new_position):
        self.current_position = new_position
        print(f"Navigation System updated position to: {self.current_position}")


class GPS:
    """
    Global Positioning System): Обеспечивает данные о местоположении для навигации и позиционирования.
    """
    pass

class IMU:
    """
    Инерциальные измерительные устройства (Inertial Measurement Units, IMUs):
    Помогают отслеживать ориентацию и движение БПЛА
    """
    pass


