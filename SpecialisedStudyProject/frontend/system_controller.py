from SpecialisedStudyProject.frontend \
    import MemoryStoreManagement


class SystemController:
    def __init__(self):
        self.memory_management: MemoryStoreManagement | None = None

    def __del__(self):
        del self.memory_management

    def get_memory_manager(self) -> MemoryStoreManagement:
        if self.is_memory_manager_none():
            self.set_memory_manager(
                MemoryStoreManagement()
            )
        return self.memory_management

    def is_memory_manager_none(self) -> bool:
        return self.memory_management is None

    def set_memory_manager(
            self,
            value: MemoryStoreManagement
    ) -> None:
        self.memory_management = value
