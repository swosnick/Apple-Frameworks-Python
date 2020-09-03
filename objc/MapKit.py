
'''
Classes from the 'MapKit' framework.
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
    
    
MKMapSnapshotter = _Class('MKMapSnapshotter')
MKBarViewOptions = _Class('MKBarViewOptions')
MKJunction = _Class('MKJunction')
MKUserLocationAnnotationViewProxy = _Class('MKUserLocationAnnotationViewProxy')
MKTransitIcon = _Class('MKTransitIcon')
MKTransitShield = _Class('MKTransitShield')
MKTransitArtwork = _Class('MKTransitArtwork')
MKWebBridge = _Class('MKWebBridge')
MKPlaceCollectionMapItem = _Class('MKPlaceCollectionMapItem')
MKMapSnapshot = _Class('MKMapSnapshot')
MKMapSnapshotFeatureAnnotation = _Class('MKMapSnapshotFeatureAnnotation')
MKMuninGroundViewInfo = _Class('MKMuninGroundViewInfo')
MKLocalSearchKeypressMetrics = _Class('MKLocalSearchKeypressMetrics')
MKThrottledGate = _Class('MKThrottledGate')
MKMapSnapshotOptions = _Class('MKMapSnapshotOptions')
MKGroupedPlacesSnapshotter = _Class('MKGroupedPlacesSnapshotter')
MKVKImageSourceKeyImageBuilder = _Class('MKVKImageSourceKeyImageBuilder')
MKVKImageSourceKeyImageResult = _Class('MKVKImageSourceKeyImageResult')
MKVKImageSourceCalculationParameters = _Class('MKVKImageSourceCalculationParameters')
MKInfoCardThemeManager = _Class('MKInfoCardThemeManager')
MKTransitItemReferenceDateUpdater = _Class('MKTransitItemReferenceDateUpdater')
MKTransitMapItemUpdater = _Class('MKTransitMapItemUpdater')
MKTileOverlayRequesterOp = _Class('MKTileOverlayRequesterOp')
MKTileOverlayTile = _Class('MKTileOverlayTile')
MKTileOverlay = _Class('MKTileOverlay')
MKPlaceCollectionsLogicController = _Class('MKPlaceCollectionsLogicController')
MKAutocompleteAnalyticsState = _Class('MKAutocompleteAnalyticsState')
MKAutocompleteAnalyticsProvider = _Class('MKAutocompleteAnalyticsProvider')
MKMapItemPhoto = _Class('MKMapItemPhoto')
MKPlaceHoursViewHelper = _Class('MKPlaceHoursViewHelper')
MKBrowseCategoryItem = _Class('MKBrowseCategoryItem')
MKDirectionsRequest = _Class('MKDirectionsRequest')
MKClusterAnnotation = _Class('MKClusterAnnotation')
MKUserLocation = _Class('MKUserLocation')
MKUserLocationInternal = _Class('MKUserLocationInternal')
MKUserLocationAnnotation = _Class('MKUserLocationAnnotation')
MKRotationFilter = _Class('MKRotationFilter')
MKLocalPointsOfInterestRequest = _Class('MKLocalPointsOfInterestRequest')
MKUserLocationHeadingLayerFactory = _Class('MKUserLocationHeadingLayerFactory')
MKPlaceCollectionsPublisherIconManager = _Class('MKPlaceCollectionsPublisherIconManager')
MKPublisherIcon = _Class('MKPublisherIcon')
MKHapticEngine = _Class('MKHapticEngine')
MKETAProvider = _Class('MKETAProvider')
MKPlaceCollectionsSizeController = _Class('MKPlaceCollectionsSizeController')
MKURLSerializer = _Class('MKURLSerializer')
MKDirections = _Class('MKDirections')
MKApplicationStateMonitor = _Class('MKApplicationStateMonitor')
MKCALayerCompletionDelegate = _Class('MKCALayerCompletionDelegate')
MKLaneDirectionCollisionCalculator = _Class('MKLaneDirectionCollisionCalculator')
MKWalletMerchantResponse = _Class('MKWalletMerchantResponse')
MKWalletMerchantStylingInfo = _Class('MKWalletMerchantStylingInfo')
MKWalletMerchantLookupRequest = _Class('MKWalletMerchantLookupRequest')
MKPlaceCollectionViewModel = _Class('MKPlaceCollectionViewModel')
MKPlaceInfoRow = _Class('MKPlaceInfoRow')
MKMuninEntryPoint = _Class('MKMuninEntryPoint')
MKRoundingByteCountFormatter = _Class('MKRoundingByteCountFormatter')
MKPlaceEncyclopedicTextItem = _Class('MKPlaceEncyclopedicTextItem')
GEOEncyclopedicInfoUserLocation = _Class('GEOEncyclopedicInfoUserLocation')
MKMuninGestureController = _Class('MKMuninGestureController')
MKTrafficSupport = _Class('MKTrafficSupport')
MKWebMessage = _Class('MKWebMessage')
MKSearchFoundationResult = _Class('MKSearchFoundationResult')
MKSearchFoundationActionItem = _Class('MKSearchFoundationActionItem')
MKSearchFoundationRichText = _Class('MKSearchFoundationRichText')
MKSearchFoundationBusinessHoursAndDistanceRichText = _Class('MKSearchFoundationBusinessHoursAndDistanceRichText')
MKSearchFoundationBusinessReviewRichText = _Class('MKSearchFoundationBusinessReviewRichText')
MKSearchFoundationImage = _Class('MKSearchFoundationImage')
MKPhotoGalleryTransitionAnimator = _Class('MKPhotoGalleryTransitionAnimator')
MKTransitDeparturesDataProvider = _Class('MKTransitDeparturesDataProvider')
MKUGCCallToActionViewAppearance = _Class('MKUGCCallToActionViewAppearance')
MKRatingStringBuilder = _Class('MKRatingStringBuilder')
MKWalletRAPReport = _Class('MKWalletRAPReport')
MKSpatialCollider = _Class('MKSpatialCollider')
MKLocalSearchSection = _Class('MKLocalSearchSection')
MKTextItemViewModel = _Class('MKTextItemViewModel')
MKThirdPartyRatingStringBuilder = _Class('MKThirdPartyRatingStringBuilder')
MKLocalSearchCompleter = _Class('MKLocalSearchCompleter')
MKSiriInteraction = _Class('MKSiriInteraction')
MKAllRouteETAsManager = _Class('MKAllRouteETAsManager')
MKTransitDeparturesDataSource = _Class('MKTransitDeparturesDataSource')
MKTransitIncidentStringProvider = _Class('MKTransitIncidentStringProvider')
MKLocalSearchResponse = _Class('MKLocalSearchResponse')
MKPlaceCollectionImageProvider = _Class('MKPlaceCollectionImageProvider')
MKWebBridgeConfiguration = _Class('MKWebBridgeConfiguration')
MKLocalSearchRequest = _Class('MKLocalSearchRequest')
MKLocalSearch = _Class('MKLocalSearch')
MKTransitDepartureServiceGapFormatterResult = _Class('MKTransitDepartureServiceGapFormatterResult')
MKTransitDepartureServiceGapFormatter = _Class('MKTransitDepartureServiceGapFormatter')
MKPlacemark = _Class('MKPlacemark')
MKMapItemMetadata = _Class('MKMapItemMetadata')
MKMapCamera = _Class('MKMapCamera')
MKMapItem = _Class('MKMapItem')
MKMapCameraZoomRange = _Class('MKMapCameraZoomRange')
MKMapAttributionImage = _Class('MKMapAttributionImage')
MKMapAttribution = _Class('MKMapAttribution')
MKSystemController = _Class('MKSystemController')
MKWebViewFactoryItem = _Class('MKWebViewFactoryItem')
MKFirstPartyRatingStringBuilder = _Class('MKFirstPartyRatingStringBuilder')
MKQuadTrie = _Class('MKQuadTrie')
MKMapSnapshotCustomFeatureAnnotation = _Class('MKMapSnapshotCustomFeatureAnnotation')
MKThreadContext = _Class('MKThreadContext')
MKUsageCounter = _Class('MKUsageCounter')
MKAnnotationViewInternal = _Class('MKAnnotationViewInternal')
MKAnnotationManager = _Class('MKAnnotationManager')
MKPlaceActivityProvider = _Class('MKPlaceActivityProvider')
MKMuninLinkPresentationActivityProvider = _Class('MKMuninLinkPresentationActivityProvider')
MKMuninURLActivityProvider = _Class('MKMuninURLActivityProvider')
MKMuninTextActivityProvider = _Class('MKMuninTextActivityProvider')
MKPlaceLocVCardActivityProvider = _Class('MKPlaceLocVCardActivityProvider')
MKPlaceMapItemActivityProvider = _Class('MKPlaceMapItemActivityProvider')
MKPlaceURLActivityProvider = _Class('MKPlaceURLActivityProvider')
MKPlaceTextActivityProvider = _Class('MKPlaceTextActivityProvider')
MKRouteActivityProvider = _Class('MKRouteActivityProvider')
MKRouteURLActivityProvider = _Class('MKRouteURLActivityProvider')
MKRouteTextActivityProvider = _Class('MKRouteTextActivityProvider')
MKRouteLinkPresentationActivityProvider = _Class('MKRouteLinkPresentationActivityProvider')
MKPlaceLinkPresentationActivityProvider = _Class('MKPlaceLinkPresentationActivityProvider')
MKPlaceViewStyleProvider = _Class('MKPlaceViewStyleProvider')
MKMapService = _Class('MKMapService')
MKPlaceActionManager = _Class('MKPlaceActionManager')
MKPlaceCardActionItem = _Class('MKPlaceCardActionItem')
MKFontManager = _Class('MKFontManager')
MKAppLaunchController = _Class('MKAppLaunchController')
MKMapsSuggestionsPredictor = _Class('MKMapsSuggestionsPredictor')
MKMapGestureController = _Class('MKMapGestureController')
MKPOIEnrichmentAvailibility = _Class('MKPOIEnrichmentAvailibility')
MKIconManager = _Class('MKIconManager')
MKRouteContextBuilder = _Class('MKRouteContextBuilder')
MKServerFormattedString = _Class('MKServerFormattedString')
MKServerFormattedStringParameters = _Class('MKServerFormattedStringParameters')
MKMapItemMetadataRequester = _Class('MKMapItemMetadataRequester')
MKMapItemMetadataRequest = _Class('MKMapItemMetadataRequest')
MKMapItemMetadataImageRequest = _Class('MKMapItemMetadataImageRequest')
MKWebViewFactory = _Class('MKWebViewFactory')
MKPlaceholderGridCache = _Class('MKPlaceholderGridCache')
MKPointOfInterestFilter = _Class('MKPointOfInterestFilter')
MKURLContext = _Class('MKURLContext')
MKTransitSectionController = _Class('MKTransitSectionController')
MKTransitDeparturesSectionController = _Class('MKTransitDeparturesSectionController')
MKTransitInactiveLinesSectionController = _Class('MKTransitInactiveLinesSectionController')
MKSizedTransitArtwork = _Class('MKSizedTransitArtwork')
MKArtworkDataSourceCache = _Class('MKArtworkDataSourceCache')
MKWhenSizedBlock = _Class('MKWhenSizedBlock')
MKMapItemIdentifier = _Class('MKMapItemIdentifier')
MKCuratedCollectionsPlacecardAnalyticsManager = _Class('MKCuratedCollectionsPlacecardAnalyticsManager')
MKTransitArtworkManager = _Class('MKTransitArtworkManager')
MKWebViewMessageHandlerProxy = _Class('MKWebViewMessageHandlerProxy')
MKWebContentBlocker = _Class('MKWebContentBlocker')
MKETAResponse = _Class('MKETAResponse')
MKShape = _Class('MKShape')
MKMultiPolygon = _Class('MKMultiPolygon')
MKMultiPolyline = _Class('MKMultiPolyline')
MKCircle = _Class('MKCircle')
MKPointAnnotation = _Class('MKPointAnnotation')
MKMultiPoint = _Class('MKMultiPoint')
MKPolygon = _Class('MKPolygon')
MKPolyline = _Class('MKPolyline')
MKGeodesicPolyline = _Class('MKGeodesicPolyline')
MKRouteStepPolyline = _Class('MKRouteStepPolyline')
MKRoutePolyline = _Class('MKRoutePolyline')
MKRouteStep = _Class('MKRouteStep')
MKRoute = _Class('MKRoute')
MKDirectionsResponse = _Class('MKDirectionsResponse')
MKOverlayRenderer = _Class('MKOverlayRenderer')
MKTileOverlayRenderer = _Class('MKTileOverlayRenderer')
MKOverlayPathRenderer = _Class('MKOverlayPathRenderer')
MKPolygonRenderer = _Class('MKPolygonRenderer')
MKCircleRenderer = _Class('MKCircleRenderer')
MKMultiPolylineRenderer = _Class('MKMultiPolylineRenderer')
MKMultiPolygonRenderer = _Class('MKMultiPolygonRenderer')
MKPolylineRenderer = _Class('MKPolylineRenderer')
MKGradientPolylineRenderer = _Class('MKGradientPolylineRenderer')
MKTransitSectionPagingFilter = _Class('MKTransitSectionPagingFilter')
MKReverseGeocoderInternal = _Class('MKReverseGeocoderInternal')
MKReverseGeocoder = _Class('MKReverseGeocoder')
MKTransitItemIncidentsController = _Class('MKTransitItemIncidentsController')
MKLocationManagerSingleUpdater = _Class('MKLocationManagerSingleUpdater')
MKLocationManager = _Class('MKLocationManager')
MKCuratedCollectionsTestManager = _Class('MKCuratedCollectionsTestManager')
MKCoreLocationProvider = _Class('MKCoreLocationProvider')
MKBlockBasedSnapshotRequester = _Class('MKBlockBasedSnapshotRequester')
MKMapSnapshotRequest = _Class('MKMapSnapshotRequest')
MKMapSnapshotCreator = _Class('MKMapSnapshotCreator')
MKPriorityToIndexMap = _Class('MKPriorityToIndexMap')
MKMapCameraBoundary = _Class('MKMapCameraBoundary')
MKURLParser = _Class('MKURLParser')
MKCollectionStorageRefiner = _Class('MKCollectionStorageRefiner')
MKTransitInfoPreload = _Class('MKTransitInfoPreload')
MKTransitInfoPreloader = _Class('MKTransitInfoPreloader')
MKPlacePublisherRefiner = _Class('MKPlacePublisherRefiner')
MKPlaceCuratedCollectionRefiner = _Class('MKPlaceCuratedCollectionRefiner')
MKMultiPartAttributedString = _Class('MKMultiPartAttributedString')
MKMapViewInternal = _Class('MKMapViewInternal')
MKMapViewLabelMarkerState = _Class('MKMapViewLabelMarkerState')
MKLocalSearchCompletion = _Class('MKLocalSearchCompletion')
MKSearchCompletion = _Class('MKSearchCompletion')
MKClipServices = _Class('MKClipServices')
MKAppleMediaServices = _Class('MKAppleMediaServices')
MKGeoJSONFeature = _Class('MKGeoJSONFeature')
MKGeoJSONDecoder = _Class('MKGeoJSONDecoder')
MKAppImageManager = _Class('MKAppImageManager')
MKFirstPartyRatingFormatter = _Class('MKFirstPartyRatingFormatter')
MKPlaceReviewAvatarGenerator = _Class('MKPlaceReviewAvatarGenerator')
MKPlaceBatchController = _Class('MKPlaceBatchController')
MKTileOverlayRequester = _Class('MKTileOverlayRequester')
MKFixedToTopCollectionViewFlowLayout = _Class('MKFixedToTopCollectionViewFlowLayout')
MKImageTextAttachment = _Class('MKImageTextAttachment')
MKEmptyTextAttachment = _Class('MKEmptyTextAttachment')
MKUserTrackingBarButtonItem = _Class('MKUserTrackingBarButtonItem')
MKTiltGestureRecognizer = _Class('MKTiltGestureRecognizer')
MKVariableDelayTapRecognizer = _Class('MKVariableDelayTapRecognizer')
MKUserLocationHeadingConeLayer = _Class('MKUserLocationHeadingConeLayer')
MKLayer = _Class('MKLayer')
MKUserLocationHeadingArrowLayer = _Class('MKUserLocationHeadingArrowLayer')
MKDistanceFormatter = _Class('MKDistanceFormatter')
MKSmallCalloutView = _Class('MKSmallCalloutView')
MKTransitIncidentItemCellBackgroundView = _Class('MKTransitIncidentItemCellBackgroundView')
MKStarRatingAndLabelView = _Class('MKStarRatingAndLabelView')
MKStarRatingView = _Class('MKStarRatingView')
MKPlaceCompleteHoursView = _Class('MKPlaceCompleteHoursView')
MKPlaceHoursView = _Class('MKPlaceHoursView')
MKPlaceServiceHoursView = _Class('MKPlaceServiceHoursView')
MKAnnotationContainerView = _Class('MKAnnotationContainerView')
MKCompassView = _Class('MKCompassView')
MKMuninContainerView = _Class('MKMuninContainerView')
MKScaleView = _Class('MKScaleView')
MKAddPhotoBadgeView = _Class('MKAddPhotoBadgeView')
MKMapItemView = _Class('MKMapItemView')
MKPlacePhotoGalleryAttributionView = _Class('MKPlacePhotoGalleryAttributionView')
MKUserTrackingButton = _Class('MKUserTrackingButton')
MKMultiPartLabel = _Class('MKMultiPartLabel')
MKThemeMultiPartLabel = _Class('MKThemeMultiPartLabel')
MKQuickLinkItemView = _Class('MKQuickLinkItemView')
MKCompassButton = _Class('MKCompassButton')
MKTransitItemIncidentView = _Class('MKTransitItemIncidentView')
MKPlaceCardActionsRowView = _Class('MKPlaceCardActionsRowView')
MKBarView = _Class('MKBarView')
MKInfoCardLoadingView = _Class('MKInfoCardLoadingView')
MKPhotoSmallAttributionView = _Class('MKPhotoSmallAttributionView')
MKUGCCallToActionLikeDislikeAccessoryView = _Class('MKUGCCallToActionLikeDislikeAccessoryView')
MKBasicMapView = _Class('MKBasicMapView')
MKPictureItemView = _Class('MKPictureItemView')
MKTextItemView = _Class('MKTextItemView')
MKAttributionLabel = _Class('MKAttributionLabel')
MKExpandingLabel = _Class('MKExpandingLabel')
MKPhotoBigAttributionView = _Class('MKPhotoBigAttributionView')
MKFirstPartyPhotoBigAttributionView = _Class('MKFirstPartyPhotoBigAttributionView')
MKThirdPartyPhotoBigAttributionView = _Class('MKThirdPartyPhotoBigAttributionView')
MKMuninContainerBadgeView = _Class('MKMuninContainerBadgeView')
MKUGCCallToActionEditAccessoryView = _Class('MKUGCCallToActionEditAccessoryView')
MKPlatterView = _Class('MKPlatterView')
MKOverlayContainerView = _Class('MKOverlayContainerView')
MKCollectionsCarouselView = _Class('MKCollectionsCarouselView')
MKOverlayView = _Class('MKOverlayView')
MKOverlayPathView = _Class('MKOverlayPathView')
MKPolylineView = _Class('MKPolylineView')
MKPolygonView = _Class('MKPolygonView')
MKCircleView = _Class('MKCircleView')
MKUGCCallToActionAddPhotosAccessoryView = _Class('MKUGCCallToActionAddPhotosAccessoryView')
MKPlaceSectionView = _Class('MKPlaceSectionView')
MKCalloutView = _Class('MKCalloutView')
MKStandardCalloutView = _Class('MKStandardCalloutView')
MKAnnotationView = _Class('MKAnnotationView')
MKUserLocationView = _Class('MKUserLocationView')
MKModernUserLocationView = _Class('MKModernUserLocationView')
MKPinAnnotationView = _Class('MKPinAnnotationView')
MKMarkerAnnotationView = _Class('MKMarkerAnnotationView')
MKMapView = _Class('MKMapView')
MKScrollContainerView = _Class('MKScrollContainerView')
MKMuninView = _Class('MKMuninView')
MKViewWithHairline = _Class('MKViewWithHairline')
MKPlaceSectionItemView = _Class('MKPlaceSectionItemView')
MKOverallRatingHeaderView = _Class('MKOverallRatingHeaderView')
MKRatingPlatterView = _Class('MKRatingPlatterView')
MKPlaceSectionHeaderView = _Class('MKPlaceSectionHeaderView')
MKPlaceSectionRowView = _Class('MKPlaceSectionRowView')
MKPlaceTextBlockCell = _Class('MKPlaceTextBlockCell')
MKServiceHoursRow = _Class('MKServiceHoursRow')
MKPlaceReservationRowView = _Class('MKPlaceReservationRowView')
MKPlaceEncyclopedicRowView = _Class('MKPlaceEncyclopedicRowView')
MKPlaceEncyclopedicFactoidView = _Class('MKPlaceEncyclopedicFactoidView')
MKPlaceTextCell = _Class('MKPlaceTextCell')
MKUGCCallToActionView = _Class('MKUGCCallToActionView')
MKPlaceInfoSuggestAnEditRowView = _Class('MKPlaceInfoSuggestAnEditRowView')
MKPlaceInfoContactRowView = _Class('MKPlaceInfoContactRowView')
MKPlaceInfoBusinessMessageRowView = _Class('MKPlaceInfoBusinessMessageRowView')
MKPlaceInfoPostalAddressRowView = _Class('MKPlaceInfoPostalAddressRowView')
MKPlaceInfoEmailRowView = _Class('MKPlaceInfoEmailRowView')
MKPlaceInfoURLRowView = _Class('MKPlaceInfoURLRowView')
MKPlaceInfoPhoneNumberView = _Class('MKPlaceInfoPhoneNumberView')
MKPlaceAttributionCell = _Class('MKPlaceAttributionCell')
MKPlaceDirectionsCell = _Class('MKPlaceDirectionsCell')
MKOfficialAppView = _Class('MKOfficialAppView')
MKPlaceHoursDayRow = _Class('MKPlaceHoursDayRow')
MKPlaceCardActionSectionView = _Class('MKPlaceCardActionSectionView')
MKPlaceReviewsViewCell = _Class('MKPlaceReviewsViewCell')
MKMuninBumpFlash = _Class('MKMuninBumpFlash')
MKIncidentFooterView = _Class('MKIncidentFooterView')
MKNearestStationLoadingCell = _Class('MKNearestStationLoadingCell')
MKNearestStationCell = _Class('MKNearestStationCell')
MKNearestStationErrorCell = _Class('MKNearestStationErrorCell')
MKTableViewCell = _Class('MKTableViewCell')
MKIncidentDetailCell = _Class('MKIncidentDetailCell')
MKIncidentExtendedDetailCell = _Class('MKIncidentExtendedDetailCell')
MKCustomSeparatorTableViewCell = _Class('MKCustomSeparatorTableViewCell')
MKTransitDeparturesSectionFooterView = _Class('MKTransitDeparturesSectionFooterView')
MKTransitDeparturesSectionHeaderView = _Class('MKTransitDeparturesSectionHeaderView')
MKTransitDeparturesCell = _Class('MKTransitDeparturesCell')
MKTransitLoadingTableViewCell = _Class('MKTransitLoadingTableViewCell')
MKTransitItemIncidentCell = _Class('MKTransitItemIncidentCell')
MKTransitSystemCell = _Class('MKTransitSystemCell')
MKTransitAttributionSummaryCell = _Class('MKTransitAttributionSummaryCell')
MKTransitMessageCell = _Class('MKTransitMessageCell')
MKBrowseCategoryCollectionViewCell = _Class('MKBrowseCategoryCollectionViewCell')
MKPlaceCollectionCell = _Class('MKPlaceCollectionCell')
MKCollectionBatchCell = _Class('MKCollectionBatchCell')
MKPlacePhotoView = _Class('MKPlacePhotoView')
MKBrowseCategoryCollectionView = _Class('MKBrowseCategoryCollectionView')
MKDebugLocationConsole = _Class('MKDebugLocationConsole')
MKPlaceAttributionLabel = _Class('MKPlaceAttributionLabel')
MKArtworkLabelView = _Class('MKArtworkLabelView')
MKTransitInfoLabelView = _Class('MKTransitInfoLabelView')
MKPlaceHeaderButton = _Class('MKPlaceHeaderButton')
MKCatalystButton = _Class('MKCatalystButton')
MKButtonWithTargetArgument = _Class('MKButtonWithTargetArgument')
MKActionRowItemView = _Class('MKActionRowItemView')
MKPlaceAttributionCellButton = _Class('MKPlaceAttributionCellButton')
MKMapSnapshotView = _Class('MKMapSnapshotView')
MKAppleLogoImageView = _Class('MKAppleLogoImageView')
MKArtworkImageView = _Class('MKArtworkImageView')
MKVibrantView = _Class('MKVibrantView')
MKVibrantLabel = _Class('MKVibrantLabel')
MKVibrantHairlineView = _Class('MKVibrantHairlineView')
MKPlacePhotoGalleryViewController = _Class('MKPlacePhotoGalleryViewController')
MKPlaceCardActionsRowViewController = _Class('MKPlaceCardActionsRowViewController')
MKAnnotatedItemListViewController = _Class('MKAnnotatedItemListViewController')
MKPictureItemContainerViewController = _Class('MKPictureItemContainerViewController')
MKPlacePhotosViewController = _Class('MKPlacePhotosViewController')
MKTextItemContainerViewController = _Class('MKTextItemContainerViewController')
MKBrowseCategoryViewController = _Class('MKBrowseCategoryViewController')
MKStackingViewController = _Class('MKStackingViewController')
MKTransitLineItemViewController = _Class('MKTransitLineItemViewController')
MKLayoutCardViewController = _Class('MKLayoutCardViewController')
MKPlaceInlineMapViewController = _Class('MKPlaceInlineMapViewController')
MKPlacePoisInlineMapViewController = _Class('MKPlacePoisInlineMapViewController')
MKPlaceSectionViewController = _Class('MKPlaceSectionViewController')
MKPlaceServiceHoursViewController = _Class('MKPlaceServiceHoursViewController')
MKPlaceReviewsViewController = _Class('MKPlaceReviewsViewController')
MKPlaceCuratedCollectionsViewController = _Class('MKPlaceCuratedCollectionsViewController')
MKPlaceHeaderButtonsViewController = _Class('MKPlaceHeaderButtonsViewController')
MKPlaceMessageViewController = _Class('MKPlaceMessageViewController')
MKPlaceInfoViewController = _Class('MKPlaceInfoViewController')
MKPlaceEncyclopedicViewController = _Class('MKPlaceEncyclopedicViewController')
MKPlaceParentInfoViewController = _Class('MKPlaceParentInfoViewController')
MKPlaceParentVenueInfoViewController = _Class('MKPlaceParentVenueInfoViewController')
MKPlaceVenueInfoContentsViewController = _Class('MKPlaceVenueInfoContentsViewController')
MKPlaceQuickLinksViewController = _Class('MKPlaceQuickLinksViewController')
MKPlaceRelatedViewController = _Class('MKPlaceRelatedViewController')
MKPlaceAttributionViewController = _Class('MKPlaceAttributionViewController')
MKPlaceReservationViewController = _Class('MKPlaceReservationViewController')
MKPlaceCardHeaderViewController = _Class('MKPlaceCardHeaderViewController')
MKUGCCallToActionViewController = _Class('MKUGCCallToActionViewController')
MKAppleRatingsViewController = _Class('MKAppleRatingsViewController')
MKOfficialAppViewController = _Class('MKOfficialAppViewController')
MKWebContentViewController = _Class('MKWebContentViewController')
MKPlaceHoursViewController = _Class('MKPlaceHoursViewController')
MKPlaceMessageHoursViewController = _Class('MKPlaceMessageHoursViewController')
MKPlaceCollectionViewController = _Class('MKPlaceCollectionViewController')
MKPlaceCardActionsViewController = _Class('MKPlaceCardActionsViewController')
MKPlaceCardFooterActionsViewController = _Class('MKPlaceCardFooterActionsViewController')
MKPlaceBusinessInfoViewController = _Class('MKPlaceBusinessInfoViewController')
MKActivityViewController = _Class('MKActivityViewController')
MKNearestStationViewController = _Class('MKNearestStationViewController')
MKTransitLineIncidentsViewController = _Class('MKTransitLineIncidentsViewController')
MKTransitDeparturesViewController = _Class('MKTransitDeparturesViewController')
MKIncidentsViewController = _Class('MKIncidentsViewController')
MKTransitAttributionViewController = _Class('MKTransitAttributionViewController')