'''
Classes from the 'MapsSync' framework.
'''

try:
    from rubicon.objc import ObjCClass
except ValueError:
    def ObjCClass(name):
        return None


def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None

    
MapsSyncEventDebouncer = _Class('MapsSync.MapsSyncEventDebouncer')
MapsSyncWrapperFactory = _Class('MapsSync.MapsSyncWrapperFactory')
MapsSyncDataBase_0_0_1 = _Class('MapsSync.MapsSyncDataBase_0_0_1')
MapsSyncDataBase_initial = _Class('MapsSync.MapsSyncDataBase_initial')
MapsSyncGeo = _Class('MapsSync.MapsSyncGeo')
MapsSyncPredicate = _Class('MapsSync.MapsSyncPredicate')
MapsSyncDataContainerXPCDelegate = _Class('MapsSync.MapsSyncDataContainerXPCDelegate')
MapsSyncXPCServer = _Class('MapsSync.MapsSyncXPCServer')
MapsSyncDataContainer = _Class('MapsSync.MapsSyncDataContainer')
MapsSyncXPCDataContainer = _Class('MapsSync.MapsSyncXPCDataContainer')
MapsSyncCloudKitDataContainer = _Class('MapsSync.MapsSyncCloudKitDataContainer')
MapsSyncMemoryOnlyDataContainer = _Class('MapsSync.MapsSyncMemoryOnlyDataContainer')
MapsSyncUtil = _Class('MapsSync.MapsSyncUtil')
MapsSyncBatch = _Class('MapsSync.MapsSyncBatch')
MapsSyncFetchedResultsControllerDelegate = _Class('MapsSync.MapsSyncFetchedResultsControllerDelegate')
MapsSyncDataSession = _Class('MapsSync.MapsSyncDataSession')
MapsSyncDataValidator = _Class('MapsSync.MapsSyncDataValidator')
MapsSyncBaseQuery = _Class('MapsSync.MapsSyncBaseQuery')
MapsSyncVehicleQuery = _Class('MapsSync.MapsSyncVehicleQuery')
MapsSyncCuratedCollectionQuery = _Class('MapsSync.MapsSyncCuratedCollectionQuery')
MapsSyncCollectionItemQuery = _Class('MapsSync.MapsSyncCollectionItemQuery')
MapsSyncFavoriteItemQuery = _Class('MapsSync.MapsSyncFavoriteItemQuery')
MapsSyncCollectionPlaceItemQuery = _Class('MapsSync.MapsSyncCollectionPlaceItemQuery')
MapsSyncCollectionTransitItemQuery = _Class('MapsSync.MapsSyncCollectionTransitItemQuery')
MapsSyncDataQuery = _Class('MapsSync.MapsSyncDataQuery')
MapsSyncCollectionQuery = _Class('MapsSync.MapsSyncCollectionQuery')
MapsSyncHistoryItemQuery = _Class('MapsSync.MapsSyncHistoryItemQuery')
MapsSyncMutableBaseItem = _Class('MapsSync.MapsSyncMutableBaseItem')
MapsSyncMutableReviewedPlace = _Class('MapsSync.MapsSyncMutableReviewedPlace')
MapsSyncMutableFavoriteItem = _Class('MapsSync.MapsSyncMutableFavoriteItem')
MapsSyncMutableAnonymousCredential = _Class('MapsSync.MapsSyncMutableAnonymousCredential')
MapsSyncMutableVehicle = _Class('MapsSync.MapsSyncMutableVehicle')
MapsSyncMutableCollection = _Class('MapsSync.MapsSyncMutableCollection')
MapsSyncMutableCuratedCollection = _Class('MapsSync.MapsSyncMutableCuratedCollection')
MapsSyncMutableHistoryItem = _Class('MapsSync.MapsSyncMutableHistoryItem')
MapsSyncMutableHistoryRideShareItem = _Class('MapsSync.MapsSyncMutableHistoryRideShareItem')
MapsSyncMutableHistorySearchItem = _Class('MapsSync.MapsSyncMutableHistorySearchItem')
MapsSyncMutableHistoryPlaceItem = _Class('MapsSync.MapsSyncMutableHistoryPlaceItem')
MapsSyncMutableHistoryTransitItem = _Class('MapsSync.MapsSyncMutableHistoryTransitItem')
MapsSyncMutableHistoryDirectionsItem = _Class('MapsSync.MapsSyncMutableHistoryDirectionsItem')
MapsSyncMutableHistoryEvDirectionsItem = _Class('MapsSync.MapsSyncMutableHistoryEvDirectionsItem')
MapsSyncMutableCachedCuratedCollection = _Class('MapsSync.MapsSyncMutableCachedCuratedCollection')
MapsSyncMutableCachedUserReview = _Class('MapsSync.MapsSyncMutableCachedUserReview')
MapsSyncMutableCollectionItem = _Class('MapsSync.MapsSyncMutableCollectionItem')
MapsSyncMutableCollectionTransitItem = _Class('MapsSync.MapsSyncMutableCollectionTransitItem')
MapsSyncMutableCollectionPlaceItem = _Class('MapsSync.MapsSyncMutableCollectionPlaceItem')
MapsSyncObjectWrapper = _Class('MapsSync.MapsSyncObjectWrapper')
MapsSyncBaseItem = _Class('MapsSync.MapsSyncBaseItem')
MapsSyncReviewedPlace = _Class('MapsSync.MapsSyncReviewedPlace')
MapsSyncFavoriteItem = _Class('MapsSync.MapsSyncFavoriteItem')
MapsSyncAnonymousCredential = _Class('MapsSync.MapsSyncAnonymousCredential')
MapsSyncVehicle = _Class('MapsSync.MapsSyncVehicle')
MapsSyncCollection = _Class('MapsSync.MapsSyncCollection')
MapsSyncCuratedCollection = _Class('MapsSync.MapsSyncCuratedCollection')
MapsSyncHistoryItem = _Class('MapsSync.MapsSyncHistoryItem')
MapsSyncHistoryRideShareItem = _Class('MapsSync.MapsSyncHistoryRideShareItem')
MapsSyncHistorySearchItem = _Class('MapsSync.MapsSyncHistorySearchItem')
MapsSyncHistoryPlaceItem = _Class('MapsSync.MapsSyncHistoryPlaceItem')
MapsSyncHistoryTransitItem = _Class('MapsSync.MapsSyncHistoryTransitItem')
MapsSyncHistoryDirectionsItem = _Class('MapsSync.MapsSyncHistoryDirectionsItem')
MapsSyncHistoryEvDirectionsItem = _Class('MapsSync.MapsSyncHistoryEvDirectionsItem')
MapsSyncCachedCuratedCollection = _Class('MapsSync.MapsSyncCachedCuratedCollection')
MapsSyncCachedUserReview = _Class('MapsSync.MapsSyncCachedUserReview')
MapsSyncCollectionItem = _Class('MapsSync.MapsSyncCollectionItem')
MapsSyncCollectionTransitItem = _Class('MapsSync.MapsSyncCollectionTransitItem')
MapsSyncCollectionPlaceItem = _Class('MapsSync.MapsSyncCollectionPlaceItem')
MapsSyncPersistentContainer = _Class('MapsSync.MapsSyncPersistentContainer')
MapsSyncManagedVehicle = _Class('MapsSyncManagedVehicle')
MapsSyncManagedCollection = _Class('MapsSyncManagedCollection')
MapsSyncManagedContactHandle = _Class('MapsSyncManagedContactHandle')
MapsSyncManagedCuratedCollection = _Class('MapsSyncManagedCuratedCollection')
MapsSyncManagedFavoriteItem = _Class('MapsSyncManagedFavoriteItem')
MapsSyncManagedHistoryItem = _Class('MapsSyncManagedHistoryItem')
MapsSyncManagedHistoryTransitItem = _Class('MapsSyncManagedHistoryTransitItem')
MapsSyncManagedHistorySearchItem = _Class('MapsSyncManagedHistorySearchItem')
MapsSyncManagedHistoryDirectionsItem = _Class('MapsSyncManagedHistoryDirectionsItem')
MapsSyncManagedHistoryEvDirectionsItem = _Class('MapsSyncManagedHistoryEvDirectionsItem')
MapsSyncManagedHistoryRideShareItem = _Class('MapsSyncManagedHistoryRideShareItem')
MapsSyncManagedHistoryPlaceItem = _Class('MapsSyncManagedHistoryPlaceItem')
MapsSyncManagedMixinMapItem = _Class('MapsSyncManagedMixinMapItem')
MapsSyncManagedCachedUserReview = _Class('MapsSyncManagedCachedUserReview')
MapsSyncManagedReviewedPlace = _Class('MapsSyncManagedReviewedPlace')
MapsSyncManagedAnonymousCredential = _Class('MapsSyncManagedAnonymousCredential')
MapsSyncManagedCachedCuratedCollection = _Class('MapsSyncManagedCachedCuratedCollection')
MapsSyncManagedCollectionItem = _Class('MapsSyncManagedCollectionItem')
MapsSyncManagedCollectionTransitItem = _Class('MapsSyncManagedCollectionTransitItem')
MapsSyncManagedCollectionPlaceItem = _Class('MapsSyncManagedCollectionPlaceItem')
MapsSyncError = _Class('MapsSync.MapsSyncError')
