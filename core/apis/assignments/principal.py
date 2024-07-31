from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment , Teacher

from .schema import AssignmentSchema, AssignmentGradeSchema , TeacherSchema
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)

@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of assignments"""
    principal_assignments = Assignment.get_assignment_by_principal()
    principal_assignments_dump = AssignmentSchema().dump(principal_assignments, many=True)
    return APIResponse.respond(data=principal_assignments_dump)

@principal_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
     """Returns list of assignments"""
     list_of_teachers = Teacher.get_teachers_by_principal()
     list_of_teachers_dump = TeacherSchema().dump(list_of_teachers,many = True)
     return APIResponse.respond(data=list_of_teachers_dump)
