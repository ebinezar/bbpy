################################################## 
# NauService_services_types.py 
# generated by ZSI.generate.wsdl2python
##################################################


import ZSI
import ZSI.TCcompound
from ZSI.schema import LocalElementDeclaration, ElementDeclaration, TypeDefinition, GTD, GED

##############################
# targetNamespace
# http://nau
##############################

class ns0:
    targetNamespace = "http://nau"

    class Exception_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://nau"
        type = (schema, "Exception")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = ns0.Exception_Def.schema
            TClist = [ZSI.TC.AnyType(pname=(ns,"Exception"), aname="_Exception", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._Exception = None
                    return
            Holder.__name__ = "Exception_Holder"
            self.pyclass = Holder

    class Exception_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "Exception"
        schema = "http://nau"
        def __init__(self, **kw):
            ns = ns0.Exception_Dec.schema
            TClist = [GTD("http://nau","Exception",lazy=False)(pname=(ns,"Exception"), aname="_Exception", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://nau","Exception")
            kw["aname"] = "_Exception"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._Exception = None
                    return
            Holder.__name__ = "Exception_Holder"
            self.pyclass = Holder

    class BatchChangeEnrollmentStatus_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "BatchChangeEnrollmentStatus"
        schema = "http://nau"
        def __init__(self, **kw):
            ns = ns0.BatchChangeEnrollmentStatus_Dec.schema
            TClist = [ZSI.TC.String(pname=(ns,"courseBatchUid"), aname="_courseBatchUid", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"peopleBatchUid"), aname="_peopleBatchUid", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.Boolean(pname=(ns,"disabled"), aname="_disabled", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://nau","BatchChangeEnrollmentStatus")
            kw["aname"] = "_BatchChangeEnrollmentStatus"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._courseBatchUid = None
                    self._peopleBatchUid = []
                    self._disabled = None
                    return
            Holder.__name__ = "BatchChangeEnrollmentStatus_Holder"
            self.pyclass = Holder

    class BatchChangeEnrollmentStatusResponse_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "BatchChangeEnrollmentStatusResponse"
        schema = "http://nau"
        def __init__(self, **kw):
            ns = ns0.BatchChangeEnrollmentStatusResponse_Dec.schema
            TClist = [ZSI.TC.Boolean(pname=(ns,"return"), aname="_return", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://nau","BatchChangeEnrollmentStatusResponse")
            kw["aname"] = "_BatchChangeEnrollmentStatusResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._return = None
                    return
            Holder.__name__ = "BatchChangeEnrollmentStatusResponse_Holder"
            self.pyclass = Holder

    class ChangeEnrollmentStatus_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "ChangeEnrollmentStatus"
        schema = "http://nau"
        def __init__(self, **kw):
            ns = ns0.ChangeEnrollmentStatus_Dec.schema
            TClist = [ZSI.TC.String(pname=(ns,"courseBatchUid"), aname="_courseBatchUid", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"personBatchUid"), aname="_personBatchUid", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.Boolean(pname=(ns,"disabled"), aname="_disabled", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://nau","ChangeEnrollmentStatus")
            kw["aname"] = "_ChangeEnrollmentStatus"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._courseBatchUid = None
                    self._personBatchUid = None
                    self._disabled = None
                    return
            Holder.__name__ = "ChangeEnrollmentStatus_Holder"
            self.pyclass = Holder

    class ChangeEnrollmentStatusResponse_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "ChangeEnrollmentStatusResponse"
        schema = "http://nau"
        def __init__(self, **kw):
            ns = ns0.ChangeEnrollmentStatusResponse_Dec.schema
            TClist = [ZSI.TC.Boolean(pname=(ns,"return"), aname="_return", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://nau","ChangeEnrollmentStatusResponse")
            kw["aname"] = "_ChangeEnrollmentStatusResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._return = None
                    return
            Holder.__name__ = "ChangeEnrollmentStatusResponse_Holder"
            self.pyclass = Holder

    class IsRolledup_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "IsRolledup"
        schema = "http://nau"
        def __init__(self, **kw):
            ns = ns0.IsRolledup_Dec.schema
            TClist = [ZSI.TC.String(pname=(ns,"parentBatchUid"), aname="_parentBatchUid", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"childBatchUid"), aname="_childBatchUid", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://nau","IsRolledup")
            kw["aname"] = "_IsRolledup"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._parentBatchUid = None
                    self._childBatchUid = None
                    return
            Holder.__name__ = "IsRolledup_Holder"
            self.pyclass = Holder

    class IsRolledupResponse_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "IsRolledupResponse"
        schema = "http://nau"
        def __init__(self, **kw):
            ns = ns0.IsRolledupResponse_Dec.schema
            TClist = [ZSI.TC.Boolean(pname=(ns,"return"), aname="_return", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://nau","IsRolledupResponse")
            kw["aname"] = "_IsRolledupResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._return = None
                    return
            Holder.__name__ = "IsRolledupResponse_Holder"
            self.pyclass = Holder

    class RollupCourse_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "RollupCourse"
        schema = "http://nau"
        def __init__(self, **kw):
            ns = ns0.RollupCourse_Dec.schema
            TClist = [ZSI.TC.String(pname=(ns,"parentBatchUid"), aname="_parentBatchUid", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"childBatchUid"), aname="_childBatchUid", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.Boolean(pname=(ns,"enable"), aname="_enable", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://nau","RollupCourse")
            kw["aname"] = "_RollupCourse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._parentBatchUid = None
                    self._childBatchUid = None
                    self._enable = None
                    return
            Holder.__name__ = "RollupCourse_Holder"
            self.pyclass = Holder

    class RollupCourseResponse_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "RollupCourseResponse"
        schema = "http://nau"
        def __init__(self, **kw):
            ns = ns0.RollupCourseResponse_Dec.schema
            TClist = [ZSI.TC.Boolean(pname=(ns,"return"), aname="_return", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://nau","RollupCourseResponse")
            kw["aname"] = "_RollupCourseResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._return = None
                    return
            Holder.__name__ = "RollupCourseResponse_Holder"
            self.pyclass = Holder

    class CreateUpdateUser_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "CreateUpdateUser"
        schema = "http://nau"
        def __init__(self, **kw):
            ns = ns0.CreateUpdateUser_Dec.schema
            TClist = [ZSI.TC.Boolean(pname=(ns,"isAvailable"), aname="_isAvailable", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"userName"), aname="_userName", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"studentId"), aname="_studentId", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"email"), aname="_email", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"firstName"), aname="_firstName", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"lastName"), aname="_lastName", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.AnyType(pname=(ns,"insRoles"), aname="_insRoles", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://nau","CreateUpdateUser")
            kw["aname"] = "_CreateUpdateUser"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._isAvailable = None
                    self._userName = None
                    self._studentId = None
                    self._email = None
                    self._firstName = None
                    self._lastName = None
                    self._insRoles = None
                    return
            Holder.__name__ = "CreateUpdateUser_Holder"
            self.pyclass = Holder

    class CreateUpdateUserResponse_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "CreateUpdateUserResponse"
        schema = "http://nau"
        def __init__(self, **kw):
            ns = ns0.CreateUpdateUserResponse_Dec.schema
            TClist = [ZSI.TC.String(pname=(ns,"return"), aname="_return", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://nau","CreateUpdateUserResponse")
            kw["aname"] = "_CreateUpdateUserResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._return = None
                    return
            Holder.__name__ = "CreateUpdateUserResponse_Holder"
            self.pyclass = Holder

    class GetIdsFromBatchUids_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "GetIdsFromBatchUids"
        schema = "http://nau"
        def __init__(self, **kw):
            ns = ns0.GetIdsFromBatchUids_Dec.schema
            TClist = [ZSI.TC.String(pname=(ns,"batchUids"), aname="_batchUids", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://nau","GetIdsFromBatchUids")
            kw["aname"] = "_GetIdsFromBatchUids"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._batchUids = []
                    return
            Holder.__name__ = "GetIdsFromBatchUids_Holder"
            self.pyclass = Holder

    class GetIdsFromBatchUidsResponse_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "GetIdsFromBatchUidsResponse"
        schema = "http://nau"
        def __init__(self, **kw):
            ns = ns0.GetIdsFromBatchUidsResponse_Dec.schema
            TClist = [ZSI.TC.String(pname=(ns,"return"), aname="_return", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://nau","GetIdsFromBatchUidsResponse")
            kw["aname"] = "_GetIdsFromBatchUidsResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._return = []
                    return
            Holder.__name__ = "GetIdsFromBatchUidsResponse_Holder"
            self.pyclass = Holder

# end class ns0 (tns: http://nau)