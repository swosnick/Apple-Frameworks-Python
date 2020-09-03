'''
Classes from the 'TrialProto' framework.
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

    
TRIPBCodedOutputStream = _Class('TRIPBCodedOutputStream')
TRIPBBoolEnumDictionary = _Class('TRIPBBoolEnumDictionary')
TRIPBBoolObjectDictionary = _Class('TRIPBBoolObjectDictionary')
TRIPBBoolDoubleDictionary = _Class('TRIPBBoolDoubleDictionary')
TRIPBBoolFloatDictionary = _Class('TRIPBBoolFloatDictionary')
TRIPBBoolBoolDictionary = _Class('TRIPBBoolBoolDictionary')
TRIPBBoolInt64Dictionary = _Class('TRIPBBoolInt64Dictionary')
TRIPBBoolUInt64Dictionary = _Class('TRIPBBoolUInt64Dictionary')
TRIPBBoolInt32Dictionary = _Class('TRIPBBoolInt32Dictionary')
TRIPBBoolUInt32Dictionary = _Class('TRIPBBoolUInt32Dictionary')
TRIPBStringEnumDictionary = _Class('TRIPBStringEnumDictionary')
TRIPBStringDoubleDictionary = _Class('TRIPBStringDoubleDictionary')
TRIPBStringFloatDictionary = _Class('TRIPBStringFloatDictionary')
TRIPBStringBoolDictionary = _Class('TRIPBStringBoolDictionary')
TRIPBStringInt64Dictionary = _Class('TRIPBStringInt64Dictionary')
TRIPBStringUInt64Dictionary = _Class('TRIPBStringUInt64Dictionary')
TRIPBStringInt32Dictionary = _Class('TRIPBStringInt32Dictionary')
TRIPBStringUInt32Dictionary = _Class('TRIPBStringUInt32Dictionary')
TRIPBInt64ObjectDictionary = _Class('TRIPBInt64ObjectDictionary')
TRIPBInt64EnumDictionary = _Class('TRIPBInt64EnumDictionary')
TRIPBInt64DoubleDictionary = _Class('TRIPBInt64DoubleDictionary')
TRIPBInt64FloatDictionary = _Class('TRIPBInt64FloatDictionary')
TRIPBInt64BoolDictionary = _Class('TRIPBInt64BoolDictionary')
TRIPBInt64Int64Dictionary = _Class('TRIPBInt64Int64Dictionary')
TRIPBInt64UInt64Dictionary = _Class('TRIPBInt64UInt64Dictionary')
TRIPBInt64Int32Dictionary = _Class('TRIPBInt64Int32Dictionary')
TRIPBInt64UInt32Dictionary = _Class('TRIPBInt64UInt32Dictionary')
TRIPBUInt64ObjectDictionary = _Class('TRIPBUInt64ObjectDictionary')
TRIPBUInt64EnumDictionary = _Class('TRIPBUInt64EnumDictionary')
TRIPBUInt64DoubleDictionary = _Class('TRIPBUInt64DoubleDictionary')
TRIPBUInt64FloatDictionary = _Class('TRIPBUInt64FloatDictionary')
TRIPBUInt64BoolDictionary = _Class('TRIPBUInt64BoolDictionary')
TRIPBUInt64Int64Dictionary = _Class('TRIPBUInt64Int64Dictionary')
TRIPBUInt64UInt64Dictionary = _Class('TRIPBUInt64UInt64Dictionary')
TRIPBUInt64Int32Dictionary = _Class('TRIPBUInt64Int32Dictionary')
TRIPBUInt64UInt32Dictionary = _Class('TRIPBUInt64UInt32Dictionary')
TRIPBInt32ObjectDictionary = _Class('TRIPBInt32ObjectDictionary')
TRIPBInt32EnumDictionary = _Class('TRIPBInt32EnumDictionary')
TRIPBInt32DoubleDictionary = _Class('TRIPBInt32DoubleDictionary')
TRIPBInt32FloatDictionary = _Class('TRIPBInt32FloatDictionary')
TRIPBInt32BoolDictionary = _Class('TRIPBInt32BoolDictionary')
TRIPBInt32Int64Dictionary = _Class('TRIPBInt32Int64Dictionary')
TRIPBInt32UInt64Dictionary = _Class('TRIPBInt32UInt64Dictionary')
TRIPBInt32Int32Dictionary = _Class('TRIPBInt32Int32Dictionary')
TRIPBInt32UInt32Dictionary = _Class('TRIPBInt32UInt32Dictionary')
TRIPBUInt32ObjectDictionary = _Class('TRIPBUInt32ObjectDictionary')
TRIPBUInt32EnumDictionary = _Class('TRIPBUInt32EnumDictionary')
TRIPBUInt32DoubleDictionary = _Class('TRIPBUInt32DoubleDictionary')
TRIPBUInt32FloatDictionary = _Class('TRIPBUInt32FloatDictionary')
TRIPBUInt32BoolDictionary = _Class('TRIPBUInt32BoolDictionary')
TRIPBUInt32Int64Dictionary = _Class('TRIPBUInt32Int64Dictionary')
TRIPBUInt32UInt64Dictionary = _Class('TRIPBUInt32UInt64Dictionary')
TRIPBUInt32Int32Dictionary = _Class('TRIPBUInt32Int32Dictionary')
TRIPBUInt32UInt32Dictionary = _Class('TRIPBUInt32UInt32Dictionary')
TRIPBEnumArray = _Class('TRIPBEnumArray')
TRIPBBoolArray = _Class('TRIPBBoolArray')
TRIPBDoubleArray = _Class('TRIPBDoubleArray')
TRIPBFloatArray = _Class('TRIPBFloatArray')
TRIPBUInt64Array = _Class('TRIPBUInt64Array')
TRIPBInt64Array = _Class('TRIPBInt64Array')
TRIPBUInt32Array = _Class('TRIPBUInt32Array')
TRIPBInt32Array = _Class('TRIPBInt32Array')
TRIPBCodedInputStream = _Class('TRIPBCodedInputStream')
TRIPBUnknownField = _Class('TRIPBUnknownField')
TRIPBExtensionRegistry = _Class('TRIPBExtensionRegistry')
TRIPBExtensionDescriptor = _Class('TRIPBExtensionDescriptor')
TRIPBEnumDescriptor = _Class('TRIPBEnumDescriptor')
TRIPBFieldDescriptor = _Class('TRIPBFieldDescriptor')
TRIPBOneofDescriptor = _Class('TRIPBOneofDescriptor')
TRIPBFileDescriptor = _Class('TRIPBFileDescriptor')
TRIPBDescriptor = _Class('TRIPBDescriptor')
TRIPBUnknownFieldSet = _Class('TRIPBUnknownFieldSet')
TRIPBRootObject = _Class('TRIPBRootObject')
TRITriprojectOwnerRoot = _Class('TRITriprojectOwnerRoot')
TRIPBApiRoot = _Class('TRIPBApiRoot')
TRIPBStructRoot = _Class('TRIPBStructRoot')
TRIPBDescriptorRoot = _Class('TRIPBDescriptorRoot')
TRIPBTypeRoot = _Class('TRIPBTypeRoot')
TRITriassignmentRoot = _Class('TRITriassignmentRoot')
TRITrideploymentEnvironmentRoot = _Class('TRITrideploymentEnvironmentRoot')
TRIPBFieldMaskRoot = _Class('TRIPBFieldMaskRoot')
TRITrinamespaceRoot = _Class('TRITrinamespaceRoot')
TRITrideploymentRoot = _Class('TRITrideploymentRoot')
TRIPBWrappersRoot = _Class('TRIPBWrappersRoot')
TRITriclientExperimentRoot = _Class('TRITriclientExperimentRoot')
TRIPBDurationRoot = _Class('TRIPBDurationRoot')
TRITricloudKitRoot = _Class('TRITricloudKitRoot')
TRITrifactorTypesRoot = _Class('TRITrifactorTypesRoot')
TRICoreMlassignmentRoot = _Class('TRICoreMlassignmentRoot')
TRIPlanOutAssignmentRoot = _Class('TRIPlanOutAssignmentRoot')
TRIPBTimestampRoot = _Class('TRIPBTimestampRoot')
TRITriuiassignmentRoot = _Class('TRITriuiassignmentRoot')
TRITrifactorRoot = _Class('TRITrifactorRoot')
TRIPBAnyRoot = _Class('TRIPBAnyRoot')
TRITriexperimentRoot = _Class('TRITriexperimentRoot')
TRIPBEmptyRoot = _Class('TRIPBEmptyRoot')
TRIPBSourceContextRoot = _Class('TRIPBSourceContextRoot')
TRIPBMessage = _Class('TRIPBMessage')
TRIProjectOwners = _Class('TRIProjectOwners')
TRIProjectOwner = _Class('TRIProjectOwner')
TRIProject = _Class('TRIProject')
TRIPBMixin = _Class('TRIPBMixin')
TRIPBMethod = _Class('TRIPBMethod')
TRIPBApi = _Class('TRIPBApi')
TRIPBListValue = _Class('TRIPBListValue')
TRIPBValue = _Class('TRIPBValue')
TRIPBStruct = _Class('TRIPBStruct')
TRIPBGeneratedCodeInfo_Annotation = _Class('TRIPBGeneratedCodeInfo_Annotation')
TRIPBGeneratedCodeInfo = _Class('TRIPBGeneratedCodeInfo')
TRIPBSourceCodeInfo_Location = _Class('TRIPBSourceCodeInfo_Location')
TRIPBSourceCodeInfo = _Class('TRIPBSourceCodeInfo')
TRIPBUninterpretedOption_NamePart = _Class('TRIPBUninterpretedOption_NamePart')
TRIPBUninterpretedOption = _Class('TRIPBUninterpretedOption')
TRIPBMethodOptions = _Class('TRIPBMethodOptions')
TRIPBServiceOptions = _Class('TRIPBServiceOptions')
TRIPBEnumValueOptions = _Class('TRIPBEnumValueOptions')
TRIPBEnumOptions = _Class('TRIPBEnumOptions')
TRIPBOneofOptions = _Class('TRIPBOneofOptions')
TRIPBFieldOptions = _Class('TRIPBFieldOptions')
TRIPBMessageOptions = _Class('TRIPBMessageOptions')
TRIPBFileOptions = _Class('TRIPBFileOptions')
TRIPBMethodDescriptorProto = _Class('TRIPBMethodDescriptorProto')
TRIPBServiceDescriptorProto = _Class('TRIPBServiceDescriptorProto')
TRIPBEnumValueDescriptorProto = _Class('TRIPBEnumValueDescriptorProto')
TRIPBEnumDescriptorProto_EnumReservedRange = _Class('TRIPBEnumDescriptorProto_EnumReservedRange')
TRIPBEnumDescriptorProto = _Class('TRIPBEnumDescriptorProto')
TRIPBOneofDescriptorProto = _Class('TRIPBOneofDescriptorProto')
TRIPBFieldDescriptorProto = _Class('TRIPBFieldDescriptorProto')
TRIPBExtensionRangeOptions = _Class('TRIPBExtensionRangeOptions')
TRIPBDescriptorProto_ReservedRange = _Class('TRIPBDescriptorProto_ReservedRange')
TRIPBDescriptorProto_ExtensionRange = _Class('TRIPBDescriptorProto_ExtensionRange')
TRIPBDescriptorProto = _Class('TRIPBDescriptorProto')
TRIPBFileDescriptorProto = _Class('TRIPBFileDescriptorProto')
TRIPBFileDescriptorSet = _Class('TRIPBFileDescriptorSet')
TRIPBOption = _Class('TRIPBOption')
TRIPBEnumValue = _Class('TRIPBEnumValue')
TRIPBEnum = _Class('TRIPBEnum')
TRIPBField = _Class('TRIPBField')
TRIPBType = _Class('TRIPBType')
TRINSExpressionAssignmentLanguage = _Class('TRINSExpressionAssignmentLanguage')
TRIAssignment = _Class('TRIAssignment')
TRIPBFieldMask = _Class('TRIPBFieldMask')
TRINamespaces = _Class('TRINamespaces')
TRINamespace = _Class('TRINamespace')
TRIApproval = _Class('TRIApproval')
TRIDeploymentRequest = _Class('TRIDeploymentRequest')
TRIRollback = _Class('TRIRollback')
TRIDeploymentTypes = _Class('TRIDeploymentTypes')
TRIDeployment = _Class('TRIDeployment')
TRIPBBytesValue = _Class('TRIPBBytesValue')
TRIPBStringValue = _Class('TRIPBStringValue')
TRIPBBoolValue = _Class('TRIPBBoolValue')
TRIPBUInt32Value = _Class('TRIPBUInt32Value')
TRIPBInt32Value = _Class('TRIPBInt32Value')
TRIPBUInt64Value = _Class('TRIPBUInt64Value')
TRIPBInt64Value = _Class('TRIPBInt64Value')
TRIPBFloatValue = _Class('TRIPBFloatValue')
TRIPBDoubleValue = _Class('TRIPBDoubleValue')
TRIClientTreatment = _Class('TRIClientTreatment')
TRIClientExperiment = _Class('TRIClientExperiment')
TRIPBDuration = _Class('TRIPBDuration')
TRICloudKit = _Class('TRICloudKit')
TRIFile = _Class('TRIFile')
TRIAsset = _Class('TRIAsset')
TRIDeploymentRule = _Class('TRIDeploymentRule')
TRICoreMLAssignmentLanguage = _Class('TRICoreMLAssignmentLanguage')
TRIPlanOutAssignmentLanguage = _Class('TRIPlanOutAssignmentLanguage')
TRIPBTimestamp = _Class('TRIPBTimestamp')
TRIUIAssignment = _Class('TRIUIAssignment')
TRIPredicate = _Class('TRIPredicate')
TRIUIAssignmentLanguage = _Class('TRIUIAssignmentLanguage')
TRIFactorLevels = _Class('TRIFactorLevels')
TRIFactorLevel = _Class('TRIFactorLevel')
TRILevel = _Class('TRILevel')
TRIFactors = _Class('TRIFactors')
TRIFactor = _Class('TRIFactor')
TRIPBAny = _Class('TRIPBAny')
TRITreatments = _Class('TRITreatments')
TRITreatment = _Class('TRITreatment')
TRINamespaceInfos = _Class('TRINamespaceInfos')
TRINamespaceInfo = _Class('TRINamespaceInfo')
TRICompatibilityVersion = _Class('TRICompatibilityVersion')
TRIExperiments = _Class('TRIExperiments')
TRIExperiment = _Class('TRIExperiment')
TRIPBEmpty = _Class('TRIPBEmpty')
TRIPBSourceContext = _Class('TRIPBSourceContext')
TRISystemDimensions = _Class('TRISystemDimensions')
TRIUserDimension = _Class('TRIUserDimension')
TRIPopulation = _Class('TRIPopulation')
TRIDenormalizedEvent = _Class('TRIDenormalizedEvent')
TRIMetric = _Class('TRIMetric')
TRILogEvent = _Class('TRILogEvent')
TRILogNamespace = _Class('TRILogNamespace')
TRILogTime = _Class('TRILogTime')
TRISubject = _Class('TRISubject')
TRILogTreatment = _Class('TRILogTreatment')
TRILogContext = _Class('TRILogContext')
TRIPBAutocreatedDictionary = _Class('TRIPBAutocreatedDictionary')
TRIPBAutocreatedArray = _Class('TRIPBAutocreatedArray')
