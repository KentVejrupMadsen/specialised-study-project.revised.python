from frontend \
    import MemoryManagement


class SystemController:
    def __init__(self):
        self.memory_management: MemoryManagement | None = None

    def __del__(self):
        del self.memory_management

    def get_memory_manager(self) -> MemoryManagement:
        if self.is_memory_manager_none():
            self.set_memory_manager(
                MemoryManagement()
            )
        return self.memory_management

    def is_memory_manager_none(self) -> bool:
        return self.memory_management is None

    def set_memory_manager(
            self,
            value: MemoryManagement
    ) -> None:
        self.memory_management = value
