#!/usr/bin/env python
from ssp.logic.templates \
    import OnFire


class OnCategoryEvent(OnFire):
    def __init__(
        self,
        category_factory_event
    ):
        super().__init__()
        self.debug_by_default()
        self.handler = category_factory_event

    def __del__(self):
        super().__del__()

    def found_token(
            self,
            value: str
    ):
        handler = self.get_category_handler()
        handler.get_entity().on_event_found_token(
            value
        )

    def get_category_handler(self):
        from ssp.builders.action_events.categories \
            import CategoryEvent
        event_handler: CategoryEvent = self.handler
        return event_handler
