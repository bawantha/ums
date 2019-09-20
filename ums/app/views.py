from flask import render_template, flash
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import expose, BaseView, has_access, AppBuilder, SimpleFormView, ModelView, IndexView
from flask_babel import lazy_gettext as _
from .models import ProgrammeType, \
    ProgrammeCollaborativeProvisionType, ProgrammeAdditionalFunding, School, NqfLevel, Award, ProgrammeNumber, Campus, \
    Programme
from . import appbuilder, db


class ProgrammeTypeModelView(ModelView):
    add_columns = {'programme_type_id', 'programme_type_name'}
    datamodel = SQLAInterface(ProgrammeType)


class ProgrammeCollaborativeProvisionTypeModelView(ModelView):
    datamodel = SQLAInterface(ProgrammeCollaborativeProvisionType)


class ProgrammeAdditionalFundingModelView(ModelView):
    datamodel = SQLAInterface(ProgrammeAdditionalFunding)


class SchoolModelView(ModelView):
    datamodel = SQLAInterface(School)
    add_columns = {'school_cd', 'school_name'}


class NqfLevelModelView(ModelView):
    datamodel = SQLAInterface(NqfLevel)
    add_columns = {'nfq_level_cd', 'nfq_level_name'}


class ProgrammeNumberModelView(ModelView):
    datamodel = SQLAInterface(ProgrammeNumber)
    list_columns = ['programme_number', 'campus_campus_cd']
    add_columns = {'programme_number', 'campus'}


class ProgrammeModelView(ModelView):
    datamodel = SQLAInterface(Programme)


class AwardModelView(ModelView):
    datamodel = SQLAInterface(Award)
    related_views = [ProgrammeModelView]
    add_columns = {'award_cd', 'award_name'}


class CampusModelView(ModelView):
    datamodel = SQLAInterface(Campus)
    related_views = [ProgrammeNumberModelView]
    add_columns = {'campus_cd', 'campus_name'}


class MyIndexView(IndexView):
    index_template = 'myindex.html'




@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()

appbuilder.add_view(
    ProgrammeTypeModelView,
    "Programme  Type",
    icon="fa-envelope",
    category="Lookups"

)

appbuilder.add_view(
    ProgrammeModelView,
    "Programme ",
    icon="fa-envelope",
    category="Programme"

)

appbuilder.add_view(
    ProgrammeCollaborativeProvisionTypeModelView,
    "Programme Collaborative Provision Type",
    icon="fa-envelope",
    category="Lookups"

)
appbuilder.add_view(
    ProgrammeAdditionalFundingModelView,
    "Programme Additional Funding",
    icon="fa-envelope",
    category="Lookups"

)

appbuilder.add_view(
    SchoolModelView,
    "School",
    icon="fa-envelope",
    category="Lookups"

)

appbuilder.add_view(
    NqfLevelModelView,
    "NqfLevel",
    icon="fa-envelope",
    category="Lookups"

)

appbuilder.add_view(
    CampusModelView,
    "Campus",
    icon="fa-envelope",
    category="Lookups",

)


appbuilder.add_view(
    ProgrammeNumberModelView,
    "Programme Number",
    icon="fa-envelope",
    category="Lookups"
)

appbuilder.add_view(
    AwardModelView,
    "Award",
    icon="fa-envelope",
    category="Lookups"

)

