from .building_create import BuildingCreateView
from .building_detail import BuildingDetailView
from .building_download import BuildingQRDownloadView
from .building_list import BuildingListView
from .building_update import BuildingUpdateView

__all__ = [
    "BuildingCreateView",
    "BuildingUpdateView",
    "BuildingListView",
    "BuildingDetailView",
    "BuildingQRDownloadView",
]
