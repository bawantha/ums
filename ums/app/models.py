from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Sequence, UniqueConstraint
from sqlalchemy.orm import relationship

# class ContactGroup(Model):
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), unique=True, nullable=False)
#
#     def __repr__(self):
#         return self.name
#
#
# class Contact(Model):
#     id = Column(Integer, primary_key=True)
#     name = Column(String(150), unique=True, nullable=False)
#     address = Column(String(564), default='Street')
#     birthday = Column(Date)
#     personal_phone = Column(String(20))
#     personal_cellphone = Column(String(20))
#     contact_group_id = Column(Integer, ForeignKey('contact_group.id'))
#     contact_group = relationship("ContactGroup")
#
#     def __repr__(self):
#         return self.name
#
#
# class Module(Model):
#     __table_args__ = {"schema": "v3"}
#     module_id = Column(Integer, primary_key=True, autoincrement=True)
#     module_cd = Column(String(10), ForeignKey('v3.module_cd.module_cd'), unique=True, nullable=False)
#     module_cd_no = Column(Integer, unique=True, )
#     module_cd_suffix = Column(String(1), unique=True)
#     module_status_cd = Column(String(10), ForeignKey('v3.module_status.module_status_cd'), nullable=False)
#     module_title = Column(String(150))
#     module_credits = Column(Integer)
#     module_status = relationship("ModuleStatus")
#     module_cd_realation = relationship("ModuleCd")
#     # module_cd_realation = relationship("ModuleCd")
#
#     # def __repr__(self):
#     #     return self.name
#
#
# class ModuleCd(Model):
#     __table_args__ = {"schema": "v3"}
#     module_cd = Column(String(10), primary_key=True, nullable=False)
#
#     def __repr__(self):
#         return self.module_cd
#
#
# class ModuleStatus(Model):
#     __table_args__ = {"schema": "v3"}
#     module_status_cd = Column(String(10), nullable=False, primary_key=True)
#     module_status_name = Column(String(25))
#
#     def __repr__(self):
#         return self.module_status_name
#
#
# #
# class ModuleCollege(Model):
#     module_college_id = Column(Integer, nullable=False, primary_key=True)
#     college_college_cd = Column(String(10), ForeignKey('college.college_cd'), nullable=False)
#     module_module_id = Column(Integer)
#
#     def __repr__(self):
#         return self.name
#
#
# class College(Model):
#     college_cd = Column(String(10), nullable=False, primary_key=True)
#     college_name = Column(String(150))
#
#     def __repr__(self):
#         return self.name
#
#
# class ModuleCampus(Model):
#     module_campus_id = Column(Integer, nullable=False, primary_key=True)
#     campus_campus_cd = Column(String(10), ForeignKey('campus.campus_cd'), nullable=False)
#     module_module_id = Column(Integer, ForeignKey('module.module_id'), nullable=False)
#
#
# class Campus(Model):
#     campus_cd = Column(Integer, nullable=False, primary_key=True)
#     campus_name = Column(String(1500), nullable=False)
#
#     def __repr__(self):
#         return self.name
#
#
# class ModuleDiscipline(Model):
#     module_discipline_id = Column(Integer, nullable=False, primary_key=True)
#     module_module_id = Column(Integer, ForeignKey('module.module_id'), nullable=False)
#     discipline_college_college_cd = Column(String(10), nullable=False)
#     discipline_id = Column(Integer, ForeignKey('discipline.discipline_id'), nullable=False)
#
#     def __repr__(self):
#         return self.name
#
#
# class Discipline(Model):
#     discipline_id = Column(Integer, nullable=False, primary_key=True),
#     college_cd = Column(String(10), ForeignKey('college.college_cd'), nullable=False),
#     discipline_cd = Column(String(10), nullable=False),
#     discipline_name = Column(String(150), nullable=False)
#
#     def __repr__(self):
#         return self.name

# class ProgrammeType(Model):
#     __table_args__ = {"schema": "v3"}
#     programme_type_id_seq = Sequence('programme_type_seq', metadata=Model.metadata)
#     programme_type_id = Column(Integer, nullable=False, primary_key=True, default=5)
#     programme_type_name = Column(String(150))
#
#     def __repr__(self):
#         return self.programme_type_name
#
#
# class ProgrammeCollaborativeProvisionType(Model):
#     __table_args__ = {"schema": "v3"}
#     programme_collaborative_provision_type_id = Column(Integer, nullable=False, primary_key=True)
#     collaborative_provision_type_text = Column(String(250))
#
#     def __repr__(self):
#         return self.collaborative_provision_type_text7
#
#
# class ProgrammeAdditionalFunding(Model):
#     __table_args__ = {"schema": "v3"}
#     programme_additional_funding_id = Column(Integer, nullable=False, primary_key=True)
#     programme_additional_funding_text = Column(String(250))
#
#     def __repr__(self):
#         return self.programme_additional_funding_text
#
#
# class School(Model):
#     __table_args__ = {"schema": "v3"}
#     school_cd = Column(String(10), nullable=False, primary_key=True)
#     school_name = Column(String(150))
#
#     def __repr__(self):
#         return self.school_name
#
#
# class NqfLevel(Model):
#     __table_args__ = {"schema": "v3"}
#     nfq_level_cd = Column(String(10), nullable=False, primary_key=True)
#     nfq_level_cd_name = Column(String(10))
#
#     def __repr__(self):
#         return self.nfq_level_cd_name
#
#
# class Campus(Model):
#     __table_args__ = {"schema": "v3"}
#     campus_cd = Column(String(10), nullable=False, primary_key=True)
#     campus_name = Column(String(150), )
#
#     def __repr__(self):
#         return self.campus_cd
#
#
# class ProgrammeNumber(Model):
#     programme_number = Column(String(10), nullable=False, primary_key=True)
#     campus_campus_cd = Column(String(10), ForeignKey('v3.campus.campus_cd'))
#     campus_name= relationship('Campus')
#
#     def __repr__(self):
#         return self.programme_number
#
#
# class Award(Model):
#     __table_args__ = {"schema": "v3"}
#     award_cd = Column(String(10), nullable=False, primary_key=True)
#     award_name = Column(String(150), )
#


### todo


from sqlalchemy import Column, Date, DateTime, ForeignKey, ForeignKeyConstraint, Integer, Numeric, String, \
    UniqueConstraint, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AcademicYear(Model):
    __tablename__ = 'academic_year'
    __table_args__ = {'schema': 'v3'}

    academic_year_id = Column(String(10), primary_key=True)
    academic_year_start_dt = Column(Date)
    academic_year_end_date = Column(Date)


class AdministrationNoteType(Model):
    __tablename__ = 'administration_note_type'
    __table_args__ = {'schema': 'v3'}

    programme_administration_note_type_id = Column(Integer, primary_key=True)
    programme_administration_note_type = Column(String(150))


class AdmissionApplicationType(Model):
    __tablename__ = 'admission_application_type'
    __table_args__ = {'schema': 'v3'}

    admission_application_type_id = Column(Integer, primary_key=True)
    admission_application_type_name = Column(String(150))


class AnticipatedStudentNumberType(Model):
    __tablename__ = 'anticipated_student_number_type'
    __table_args__ = {'schema': 'v3'}

    anticipated_student_number_type_id = Column(Integer, primary_key=True)
    anticipated_student_type_name = Column(String(150))


class ApplicationProcedureType(Model):
    __tablename__ = 'application_procedure_type'
    __table_args__ = {'schema': 'v3'}

    application_procedure_type_id = Column(Integer, primary_key=True)
    application_procedure_type_name = Column(String(150))


class AssessmentFeedbackType(Model):
    __tablename__ = 'assessment_feedback_type'
    __table_args__ = {'schema': 'v3'}

    assessment_feedback_type_cd = Column(String(10), primary_key=True)
    assessment_feedback_type_name = Column(String(150))


class Award(Model):
    __tablename__ = 'award'
    __table_args__ = {'schema': 'v3'}

    award_cd = Column(String(10), primary_key=True)
    award_name = Column(String(150))

    def __repr__(self):
        return self.award_name


class BenchmarkAchievementLevel(Model):
    __tablename__ = 'benchmark_achievement_level'
    __table_args__ = {'schema': 'v3'}

    benchmark_achievement_level_id = Column(Numeric, primary_key=True)
    benchmark_achievement_level_name = Column(String(150))


class BenchmarkLearningOutcomeAuthority(Model):
    __tablename__ = 'benchmark_learning_outcome_authority'
    __table_args__ = {'schema': 'v3'}

    benchmark_learning_outcome_authority_id = Column(Numeric, primary_key=True)
    benchmark_learning_outcome_name = Column(String(150))


class Campus(Model):
    __tablename__ = 'campus'
    __table_args__ = {'schema': 'v3'}

    campus_cd = Column(String(10), primary_key=True)
    campus_name = Column(String(150))

    def __repr__(self):
        return self.campus_name


class College(Model):
    __tablename__ = 'college'
    __table_args__ = {'schema': 'v3'}

    college_cd = Column(String(10), primary_key=True)
    college_name = Column(String(150))


class CourseDeliveryInitiative(Model):
    __tablename__ = 'course_delivery_initiative'
    __table_args__ = {'schema': 'v3'}

    course_delivery_initiative_id = Column(Integer, primary_key=True)
    course_delivery_initiative_name = Column(String(550))


class DbsCheckLevel(Model):
    __tablename__ = 'dbs_check_level'
    __table_args__ = {'schema': 'v3'}

    dbs_check_level_id = Column(Integer, primary_key=True)
    dbs_check_level_name = Column(String(150))


class FeeStudentType(Model):
    __tablename__ = 'fee_student_type'
    __table_args__ = {'schema': 'v3'}

    fee_student_type_id = Column(Integer, primary_key=True)
    fee_student_type_name = Column(String(150))


class FormOfAssessmentType(Model):
    __tablename__ = 'form_of_assessment_type'
    __table_args__ = {'schema': 'v3'}

    form_of_assessment_type_cd = Column(String(10), primary_key=True)
    form_of_assessment_type_name = Column(String(150))


class IntendedLearningOutcomeCd(Model):
    __tablename__ = 'intended_learning_outcome_cd'
    __table_args__ = {'schema': 'v3'}

    intended_learning_outcome_cd = Column(String(10), primary_key=True)
    intended_learning_outcome_name = Column(String(150))


class LearningActivitiesCategory(Model):
    __tablename__ = 'learning_activities_category'
    __table_args__ = {'schema': 'v3'}

    learning_activities_category_cd = Column(String(10), primary_key=True)
    learning_activities_category_name = Column(String(150))


class ModuleAssessmentType(Model):
    __tablename__ = 'module_assessment_type'
    __table_args__ = {'schema': 'v3'}

    module_assessment_type_cd = Column(String(10), primary_key=True)
    module_assessment_type_name = Column(String(150))


class ModuleAssociationGroupType(Model):
    __tablename__ = 'module_association_group_type'
    __table_args__ = {'schema': 'v3'}

    module_association_group_type_id = Column(Numeric, primary_key=True)
    module_association_group_action = Column(String(150))


class ModuleAssociationType(Model):
    __tablename__ = 'module_association_type'
    __table_args__ = {'schema': 'v3'}

    module_association_type_id = Column(Numeric, primary_key=True)
    module_association_name = Column(String(150))


class ModuleCd(Model):
    __tablename__ = 'module_cd'
    __table_args__ = {'schema': 'v3'}

    module_cd = Column(String(10), primary_key=True)


class ModuleInstanceGroup(Model):
    __tablename__ = 'module_instance_group'
    __table_args__ = {'schema': 'v3'}

    module_group_id = Column(Numeric, primary_key=True)
    module_group_description = Column(String(7000))
    optional_or_mandatory_group_ind = Column(String(1))


class ModuleLearningResourceType(Model):
    __tablename__ = 'module_learning_resource_type'
    __table_args__ = {'schema': 'v3'}

    module_learning_resource_type_cd = Column(String(10), primary_key=True)
    module_learning_resources_type_name = Column(String(150))


class ModuleNqfLevelCd(Model):
    __tablename__ = 'module_nqf_level_cd'
    __table_args__ = {'schema': 'v3'}

    module_nqf_level_cd = Column(String(10), primary_key=True)
    module_nqf_level_description = Column(String(550))


class ModuleStaffRole(Model):
    __tablename__ = 'module_staff_role'
    __table_args__ = {'schema': 'v3'}

    module_staff_role_id = Column(Numeric, primary_key=True)
    module_staff_role_name = Column(String(150))


class ModuleStatus(Model):
    __tablename__ = 'module_status'
    __table_args__ = {'schema': 'v3'}

    module_status_cd = Column(String(10), primary_key=True)
    module_status_name = Column(String(25))


class NqfLevel(Model):
    __tablename__ = 'nqf_level'
    __table_args__ = {'schema': 'v3'}

    nfq_level_cd = Column(String(10), primary_key=True)
    nfq_level_name = Column(String(10))

    def __repr__(self):
        return self.nfq_level_name


class PartnerInstitutionType(Model):
    __tablename__ = 'partner_institution_type'
    __table_args__ = {'schema': 'v3'}

    partner_institution_type_id = Column(Integer, primary_key=True)
    partner_institution_type_name = Column(String(150))


class PathwayType(Model):
    __tablename__ = 'pathway_type'
    __table_args__ = {'schema': 'v3'}

    pathway_type_id = Column(Integer, primary_key=True)
    pathway_type_name = Column(String(150))


class ProgrammeAccreditationBody(Model):
    __tablename__ = 'programme_accreditation_body'
    __table_args__ = {'schema': 'v3'}

    programme_accreditation_body_code = Column(String(10), primary_key=True)
    programme_accreditation_body_name = Column(String(7000))


class ProgrammeAccreditationType(Model):
    __tablename__ = 'programme_accreditation_type'
    __table_args__ = {'schema': 'v3'}

    programme_accreditation_type_code = Column(String(10), primary_key=True)
    progeamme_accreditation_type_name = Column(String(150))


class ProgrammeAdditionalFunding(Model):
    __tablename__ = 'programme_additional_funding'
    __table_args__ = {'schema': 'v3'}

    programme_additional_funding_id = Column(Integer, primary_key=True, autoincrement=True, default=text(
        "nextval('v3.programme_additional_funding_programme_additional_funding_i_seq'::regclass)"))
    programme_additional_funding_text = Column(String(10))

    def __repr__(self):
        return self.programme_additional_funding_text;


class ProgrammeCollaborativeProvisionType(Model):
    __tablename__ = 'programme_collaborative_provision_type'
    __table_args__ = {'schema': 'v3'}

    programme_collaborative_provision_type_id = Column(Integer, primary_key=True, )
    collaborative_provision_type_text = Column(String(250))

    def __repr__(self):
        return self.collaborative_provision_type_text


class ProgrammeContactType(Model):
    __tablename__ = 'programme_contact_type'
    __table_args__ = {'schema': 'v3'}

    prgoramme_contact_type_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_contact_type_prgoramme_contact_type_id_seq'::regclass)"))
    programme_contact_type_name = Column(String(150))


class ProgrammeDeliveryMode(Model):
    __tablename__ = 'programme_delivery_mode'
    __table_args__ = {'schema': 'v3'}

    programme_delivery_mode_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_delivery_mode_programme_delivery_mode_id_seq'::regclass)"))
    programme_delivery_mode_name = Column(String(150))

    def __repr__(self):
        return self.programme_delivery_mode_name;


class ProgrammeLearningOutcomeType(Model):
    __tablename__ = 'programme_learning_outcome_type'
    __table_args__ = {'schema': 'v3'}

    programme_learning_outcome_type_cd = Column(Numeric, primary_key=True)
    programme_learning_outcome_type_name = Column(String(150))


class ProgrammeLength(Model):
    __tablename__ = 'programme_length'
    __table_args__ = {'schema': 'v3'}

    programme_length_cd = Column(String(10), primary_key=True)
    programme_length_years = Column(Numeric)
    def __repr__(self):
        return str(self.programme_length_years);


class ProgrammePgceFundingType(Model):
    __tablename__ = 'programme_pgce_funding_type'
    __table_args__ = {'schema': 'v3'}

    programme_pgce_funding_type = Column(Integer, primary_key=True)
    programme_pgce_funding_type_name = Column(String(150))

    def __repr__(self):
        return self.programme_pgce_funding_type_name


class ProgrammeProgressionType(Model):
    __tablename__ = 'programme_progression_type'
    __table_args__ = {'schema': 'v3'}

    programme_progression_type_id = Column(Integer, primary_key=True, autoincrement=True)
    programme_progression_type_name = Column(String(250))


class ProgrammePsrbType(Model):
    __tablename__ = 'programme_psrb_type'
    __table_args__ = {'schema': 'v3'}

    programme_psrb_type_id = Column(Integer, primary_key=True)
    programme_psrb_name = Column(String(150))


class ProgrammeRootCode(Model):
    __tablename__ = 'programme_root_code'
    __table_args__ = {'schema': 'v3'}

    programme_root_cd = Column(String(10), primary_key=True)
    programme_root_code_name = Column(String(150))

    def __repr__(self):
        return  self.programme_root_code_name;


class ProgrammeStatusType(Model):
    __tablename__ = 'programme_status_type'
    __table_args__ = {'schema': 'v3'}

    programme_status_type_cd = Column(String(10), primary_key=True)
    programme_status_name = Column(String(150))

    def __repr__(self):
        return  self.programme_status_name


class ProgrammeSubmission(Model):
    __tablename__ = 'programme_submission'
    __table_args__ = {'schema': 'v3'}

    programme_submission_id = Column(Numeric, primary_key=True)

    def __repr__(self):
        return str(self.programme_submission_id)





class ProgrammeType(Model):
    __tablename__ = 'programme_type'
    __table_args__ = {'schema': 'v3'}

    programme_type_id = Column(Numeric, primary_key=True)
    programme_type_name = Column(String(150))

    def __repr__(self):
        return self.programme_type_name


class ProgrammeVariantType(Model):
    __tablename__ = 'programme_variant_type'
    __table_args__ = {'schema': 'v3'}

    programme_variant_type_id = Column(Integer, primary_key=True)
    programme_variant_type_name = Column(String(150))

    def __repr__(self):
        return  self.programme_variant_type_name


class ReassessmentTimescale(Model):
    __tablename__ = 'reassessment_timescale'
    __table_args__ = {'schema': 'v3'}

    reassessment_timescale_id = Column(Numeric, primary_key=True)
    reassessment_timescale_name = Column(String(150))


class ReportingAttribute(Model):
    __tablename__ = 'reporting_attribute'
    __table_args__ = {'schema': 'v3'}

    reporting_attribute_id = Column(Integer, primary_key=True)
    reporting_attribute_code = Column(String(10), nullable=False)
    reporting_attribute_name = Column(String(150))


class SandwichCourseType(Model):
    __tablename__ = 'sandwich_course_type'
    __table_args__ = {'schema': 'v3'}

    sandwich_course_type_id = Column(Integer, primary_key=True)
    sandwich_course_type_name = Column(String(150))


class School(Model):
    __tablename__ = 'school'
    __table_args__ = {'schema': 'v3'}

    school_cd = Column(String(10), primary_key=True)
    school_name = Column(String(150))

    def __repr__(self):
        return self.school_name


class StaffSourceApplication(Model):
    __tablename__ = 'staff_source_application'
    __table_args__ = {'schema': 'v3'}

    source_application_id = Column(Numeric, primary_key=True)
    source_application_name = Column(String(150))


class StudentCohort(Model):
    __tablename__ = 'student_cohort'
    __table_args__ = {'schema': 'v3'}

    student_cohort_id = Column(Numeric, primary_key=True)


class StudyMode(Model):
    __tablename__ = 'study_mode'
    __table_args__ = {'schema': 'v3'}

    study_mode_cd = Column(Numeric, primary_key=True)
    study_mode_name = Column(String(150))


class SubmissionApprovalType(Model):
    __tablename__ = 'submission_approval_type'
    __table_args__ = {'schema': 'v3'}

    submission_approval_type_id = Column(Integer, primary_key=True)
    submission_apprval_type_name = Column(String(150))


class SubmissionAuthorisationRole(Model):
    __tablename__ = 'submission_authorisation_role'
    __table_args__ = {'schema': 'v3'}

    authorisation_role_id = Column(Integer, primary_key=True)
    authorisation_role_name = Column(String(150))


class TeacherTrainingCourseType(Model):
    __tablename__ = 'teacher_training_course_type'
    __table_args__ = {'schema': 'v3'}

    teacher_training_course_type_id = Column(Integer, primary_key=True)
    teacher_training_course_type_name = Column(String(250))


class BenchmarkLearningOutcomeType(Model):
    __tablename__ = 'benchmark_learning_outcome_type'
    __table_args__ = {'schema': 'v3'}

    benchmark_learning_outcome_type_id = Column(Numeric, primary_key=True)
    benchmark_learning_outcome_type_authority_id = Column(
        ForeignKey('v3.benchmark_learning_outcome_authority.benchmark_learning_outcome_authority_id',
                   ondelete='CASCADE'), nullable=False)
    benchmark_learning_type_name = Column(String(150))

    benchmark_learning_outcome_type_authority = relationship('BenchmarkLearningOutcomeAuthority')


class CollegeCampu(Model):
    __tablename__ = 'college_campus'
    __table_args__ = {'schema': 'v3'}

    college_campus_id = Column(Numeric, primary_key=True)
    college_college_cd = Column(ForeignKey('v3.college.college_cd', ondelete='CASCADE'), nullable=False)
    campus_campus_cd = Column(ForeignKey('v3.campus.campus_cd', ondelete='CASCADE'), nullable=False)

    campus = relationship('Campus')
    college = relationship('College')


class Discipline(Model):
    __tablename__ = 'discipline'
    __table_args__ = {'schema': 'v3'}

    discipline_id = Column(Numeric, primary_key=True)
    college_cd = Column(ForeignKey('v3.college.college_cd', ondelete='CASCADE'), nullable=False)
    discipline_cd = Column(String(10), nullable=False)
    discipline_name = Column(String(150))

    college = relationship('College')


class Module(Model):
    __tablename__ = 'module'
    __table_args__ = (
        UniqueConstraint('module_cd', 'module_cd_no', 'module_cd_suffix'),
        {'schema': 'v3'}
    )

    module_id = Column(Integer, primary_key=True, server_default=text("nextval('v3.module_module_id_seq'::regclass)"))
    module_cd = Column(ForeignKey('v3.module_cd.module_cd', ondelete='CASCADE'), nullable=False)
    module_cd_no = Column(Numeric)
    module_cd_suffix = Column(String(1))
    module_status_cd = Column(ForeignKey('v3.module_status.module_status_cd', ondelete='CASCADE'), nullable=False)
    module_title = Column(String(150))
    module_credits = Column(Numeric)

    module_cd1 = relationship('ModuleCd')
    module_status = relationship('ModuleStatus')


class ModuleAssociationGroup(Model):
    __tablename__ = 'module_association_group'
    __table_args__ = {'schema': 'v3'}

    module_association_group_id = Column(Numeric, primary_key=True)
    module_association_group_type_id = Column(
        ForeignKey('v3.module_association_group_type.module_association_group_type_id', ondelete='CASCADE'),
        nullable=False)
    number_of_modules_required = Column(Numeric)

    module_association_group_type = relationship('ModuleAssociationGroupType')


class PartnerInstitution(Model):
    __tablename__ = 'partner_institution'
    __table_args__ = {'schema': 'v3'}

    partner_institution_cd = Column(String(10), primary_key=True)
    partner_institution_name = Column(String(150))
    partner_institution_type_id = Column(
        ForeignKey('v3.partner_institution_type.partner_institution_type_id', ondelete='CASCADE'), nullable=False)
    other_partner_institution_type = Column(String(150))

    partner_institution_type = relationship('PartnerInstitutionType')


class ProgrammeNumber(Model):
    __tablename__ = 'programme_number'
    __table_args__ = {'schema': 'v3'}

    programme_number = Column(String(10), primary_key=True)
    campus_campus_cd = Column(ForeignKey('v3.campus.campus_cd', ondelete='CASCADE'))

    campus = relationship('Campus')

    def __repr__(self):
        return self.programme_number;


class Staff(Model):
    __tablename__ = 'staff'
    __table_args__ = {'schema': 'v3'}

    staff_id = Column(String(10), primary_key=True, nullable=False)
    staff_email = Column(String(150), primary_key=True, nullable=False)
    source_application_id = Column(ForeignKey('v3.staff_source_application.source_application_id', ondelete='CASCADE'),
                                   nullable=False)
    staff_name = Column(String(150))
    staff_phone_number = Column(String(150))
    mandually_entered_indicator = Column(String(1))

    source_application = relationship('StaffSourceApplication')


class BenchmarkLearningOutcome(Model):
    __tablename__ = 'benchmark_learning_outcome'
    __table_args__ = {'schema': 'v3'}

    benchmark_learning_outcome_id = Column(Numeric, primary_key=True)
    benchmark_learning_outcome_type_id = Column(
        ForeignKey('v3.benchmark_learning_outcome_type.benchmark_learning_outcome_type_id', ondelete='CASCADE'),
        nullable=False)
    benchmark_learning_outcome_authority_id = Column(
        ForeignKey('v3.benchmark_learning_outcome_authority.benchmark_learning_outcome_authority_id',
                   ondelete='CASCADE'), nullable=False)
    benchmark_learning_outcome_description = Column(String(550))

    benchmark_learning_outcome_authority = relationship('BenchmarkLearningOutcomeAuthority')
    benchmark_learning_outcome_type = relationship('BenchmarkLearningOutcomeType')


class ModuleCampu(Model):
    __tablename__ = 'module_campus'
    __table_args__ = {'schema': 'v3'}

    module_campus_id = Column(Integer, primary_key=True,
                              server_default=text("nextval('v3.module_campus_module_campus_id_seq'::regclass)"))
    campus_campus_cd = Column(ForeignKey('v3.campus.campus_cd', ondelete='CASCADE'), nullable=False)
    module_module_id = Column(ForeignKey('v3.module.module_id', ondelete='CASCADE'), nullable=False)

    campus = relationship('Campus')
    module_module = relationship('Module')


class ModuleCollege(Model):
    __tablename__ = 'module_college'
    __table_args__ = {'schema': 'v3'}

    module_college_id = Column(Integer, primary_key=True,
                               server_default=text("nextval('v3.module_college_module_college_id_seq'::regclass)"))
    college_college_cd = Column(ForeignKey('v3.college.college_cd', ondelete='CASCADE'), nullable=False)
    module_module_id = Column(ForeignKey('v3.module.module_id', ondelete='CASCADE'), nullable=False)
    college_pct_ownership = Column(Numeric)

    college = relationship('College')
    module_module = relationship('Module')


class ModuleDiscipline(Model):
    __tablename__ = 'module_discipline'
    __table_args__ = {'schema': 'v3'}

    module_discipline_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.module_discipline_module_discipline_id_seq'::regclass)"))
    module_module_id = Column(ForeignKey('v3.module.module_id', ondelete='CASCADE'), nullable=False)
    discipline_id = Column(ForeignKey('v3.discipline.discipline_id', ondelete='CASCADE'), nullable=False)

    discipline = relationship('Discipline')
    module_module = relationship('Module')


class ModuleInstance(Model):
    __tablename__ = 'module_instance'
    __table_args__ = {'schema': 'v3'}

    module_instance_id = Column(Integer, primary_key=True,
                                server_default=text("nextval('v3.module_instance_module_instance_id_seq'::regclass)"))
    module_module_id = Column(ForeignKey('v3.module.module_id', ondelete='CASCADE'), nullable=False)
    academic_year_id = Column(ForeignKey('v3.academic_year.academic_year_id', ondelete='CASCADE'), nullable=False)
    module_nqf_level_cd = Column(ForeignKey('v3.module_nqf_level_cd.module_nqf_level_cd', ondelete='CASCADE'),
                                 nullable=False)
    anticipated_student_num_taking_module = Column(Numeric)
    maximum_student_num_for_module = Column(Numeric)
    module_description = Column(String(7000))
    module_aims = Column(String(7000))
    syllabus_plan = Column(String(7000))
    active_ele_page_ind = Column(String(1))
    created_dt = Column(Date)
    last_reviewed_dt = Column(Date)
    updated_dt = Column(Date)
    updated_by = Column(String(150))

    academic_year = relationship('AcademicYear')
    module_module = relationship('Module')
    module_nqf_level_cd1 = relationship('ModuleNqfLevelCd')


class ModuleReportingAttribute(Model):
    __tablename__ = 'module_reporting_attribute'
    __table_args__ = {'schema': 'v3'}

    module_reporting_attribute_id = Column(Numeric, primary_key=True)
    module_module_id = Column(ForeignKey('v3.module.module_id', ondelete='CASCADE'), nullable=False)
    reporting_attribute_id = Column(ForeignKey('v3.reporting_attribute.reporting_attribute_id', ondelete='CASCADE'),
                                    nullable=False)

    module_module = relationship('Module')
    reporting_attribute = relationship('ReportingAttribute')


class ProgrammeSubmissionNote(Model):
    __tablename__ = 'programme_submission_note'
    __table_args__ = (
        ForeignKeyConstraint(['staff_id', 'staff_email'], ['v3.staff.staff_id', 'v3.staff.staff_email'],
                             ondelete='CASCADE'),
        {'schema': 'v3'}
    )

    programme_submission_note_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_submission_note_programme_submission_note_id_seq'::regclass)"))
    programme_submission_id = Column(ForeignKey('v3.programme_submission.programme_submission_id', ondelete='CASCADE'),
                                     nullable=False)
    staff_id = Column(String(10), nullable=False)
    staff_email = Column(String(150), nullable=False)
    note_text = Column(String(7000))
    note_date_time = Column(DateTime)

    programme_submission = relationship('ProgrammeSubmission')
    staff = relationship('Staff')


class SubDiscipline(Model):
    __tablename__ = 'sub_discipline'
    __table_args__ = {'schema': 'v3'}

    discipline_college_college_cd = Column(String(10), primary_key=True, nullable=False)
    discipline_discipline_cd = Column(String(10), primary_key=True, nullable=False)
    sub_discipline_cd = Column(String(10), primary_key=True, nullable=False)
    sub_discipline_name = Column(String(150))
    discipline_id = Column(ForeignKey('v3.discipline.discipline_id', ondelete='CASCADE'), nullable=False)

    discipline = relationship('Discipline')


class SubmissionApproval(Model):
    __tablename__ = 'submission_approval'
    __table_args__ = {'schema': 'v3'}

    submission_approval_id = Column(Integer, primary_key=True)
    authorisation_role_id = Column(
        ForeignKey('v3.submission_authorisation_role.authorisation_role_id', ondelete='CASCADE'), nullable=False)
    programme_submission_id = Column(ForeignKey('v3.programme_submission.programme_submission_id', ondelete='CASCADE'),
                                     nullable=False)
    submission_approval_type_id = Column(
        ForeignKey('v3.submission_approval_type.submission_approval_type_id', ondelete='CASCADE'), nullable=False)
    partner_institution_cd = Column(ForeignKey('v3.partner_institution.partner_institution_cd', ondelete='CASCADE'))
    submission_approval_date = Column(Date)
    submission_approval_person_name = Column(String(150))

    authorisation_role = relationship('SubmissionAuthorisationRole')
    partner_institution = relationship('PartnerInstitution')
    programme_submission = relationship('ProgrammeSubmission')
    submission_approval_type = relationship('SubmissionApprovalType')


class BenchmarkLearningOutcomeMeasure(Model):
    __tablename__ = 'benchmark_learning_outcome_measure'
    __table_args__ = {'schema': 'v3'}

    benchmark_learning_outcome_measure_id = Column(Numeric, primary_key=True)
    benchmark_learning_outcome_id = Column(
        ForeignKey('v3.benchmark_learning_outcome.benchmark_learning_outcome_id', ondelete='CASCADE'), nullable=False)
    benchmark_achievement_level_id = Column(
        ForeignKey('v3.benchmark_achievement_level.benchmark_achievement_level_id', ondelete='CASCADE'), nullable=False)
    benchmark_learning_outcome_measure_description = Column(String(550))

    benchmark_achievement_level = relationship('BenchmarkAchievementLevel')
    benchmark_learning_outcome = relationship('BenchmarkLearningOutcome')


class ModuleAssessment(Model):
    __tablename__ = 'module_assessment'
    __table_args__ = {'schema': 'v3'}

    module_assessment_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.module_assessment_module_assessment_id_seq'::regclass)"))
    module_assessment_type_cd = Column(
        ForeignKey('v3.module_assessment_type.module_assessment_type_cd', ondelete='CASCADE'), nullable=False)
    form_of_assessment_type_cd = Column(
        ForeignKey('v3.form_of_assessment_type.form_of_assessment_type_cd', ondelete='CASCADE'), nullable=False)
    module_instance_id = Column(ForeignKey('v3.module_instance.module_instance_id', ondelete='CASCADE'), nullable=False)
    assessment_feedback_type_cd = Column(
        ForeignKey('v3.assessment_feedback_type.assessment_feedback_type_cd', ondelete='CASCADE'), nullable=False)
    assessment_size = Column(String(550))
    module_assessment_credit_pct = Column(Numeric)

    assessment_feedback_type = relationship('AssessmentFeedbackType')
    form_of_assessment_type = relationship('FormOfAssessmentType')
    module_assessment_type = relationship('ModuleAssessmentType')
    module_instance = relationship('ModuleInstance')


class ModuleAssociation(Model):
    __tablename__ = 'module_association'
    __table_args__ = {'schema': 'v3'}

    module_association_id = Column(Numeric, primary_key=True)
    module_association_type_module_association_type_id = Column(
        ForeignKey('v3.module_association_type.module_association_type_id', ondelete='CASCADE'), nullable=False)
    first_module_instance_module_instance_id = Column(
        ForeignKey('v3.module_instance.module_instance_id', ondelete='CASCADE'), nullable=False)
    second_module_instance_module_instance_id = Column(
        ForeignKey('v3.module_instance.module_instance_id', ondelete='CASCADE'), nullable=False)
    module_association_group_module_association_group_id = Column(
        ForeignKey('v3.module_association_group.module_association_group_id', ondelete='CASCADE'), nullable=False)

    first_module_instance_module_instance = relationship('ModuleInstance',
                                                         primaryjoin='ModuleAssociation.first_module_instance_module_instance_id == ModuleInstance.module_instance_id')
    module_association_group_module_association_group = relationship('ModuleAssociationGroup')
    module_association_type_module_association_type = relationship('ModuleAssociationType')
    second_module_instance_module_instance = relationship('ModuleInstance',
                                                          primaryjoin='ModuleAssociation.second_module_instance_module_instance_id == ModuleInstance.module_instance_id')


class ModuleDeferredReassessment(Model):
    __tablename__ = 'module_deferred_reassessment'
    __table_args__ = {'schema': 'v3'}

    module_deferred_reassessment_id = Column(Numeric, primary_key=True)
    module_instance_module_instance_id = Column(ForeignKey('v3.module_instance.module_instance_id', ondelete='CASCADE'),
                                                nullable=False)
    original_form_of_assessment_type_cd = Column(
        ForeignKey('v3.form_of_assessment_type.form_of_assessment_type_cd', ondelete='CASCADE'), nullable=False)
    defered_form_of_reassessment_type_cd = Column(
        ForeignKey('v3.form_of_assessment_type.form_of_assessment_type_cd', ondelete='CASCADE'), nullable=False)
    deferred_reassessment_timescale_id = Column(
        ForeignKey('v3.reassessment_timescale.reassessment_timescale_id', ondelete='CASCADE'), nullable=False)
    deferred_reassessment_notes = Column(String(7000))

    form_of_assessment_type = relationship('FormOfAssessmentType',
                                           primaryjoin='ModuleDeferredReassessment.defered_form_of_reassessment_type_cd == FormOfAssessmentType.form_of_assessment_type_cd')
    deferred_reassessment_timescale = relationship('ReassessmentTimescale')
    module_instance_module_instance = relationship('ModuleInstance')
    form_of_assessment_type1 = relationship('FormOfAssessmentType',
                                            primaryjoin='ModuleDeferredReassessment.original_form_of_assessment_type_cd == FormOfAssessmentType.form_of_assessment_type_cd')


class ModuleInstanceGroupModule(Model):
    __tablename__ = 'module_instance_group_modules'
    __table_args__ = {'schema': 'v3'}

    module_instance_group_modules_id = Column(Numeric, primary_key=True)
    module_instance_id = Column(ForeignKey('v3.module_instance.module_instance_id', ondelete='CASCADE'), nullable=False)
    module_group_id = Column(ForeignKey('v3.module_instance_group.module_group_id', ondelete='CASCADE'), nullable=False)

    module_group = relationship('ModuleInstanceGroup')
    module_instance = relationship('ModuleInstance')


class ModuleIntendedLearningOutcome(Model):
    __tablename__ = 'module_intended_learning_outcomes'
    __table_args__ = {'schema': 'v3'}

    module_instance_module_instance_id = Column(ForeignKey('v3.module_instance.module_instance_id', ondelete='CASCADE'),
                                                primary_key=True, nullable=False)
    module_order_no = Column(Numeric, primary_key=True, nullable=False)
    learning_outcome_description = Column(String(7000))
    intended_learning_outcome_cd = Column(
        ForeignKey('v3.intended_learning_outcome_cd.intended_learning_outcome_cd', ondelete='CASCADE'), nullable=False)

    intended_learning_outcome_cd1 = relationship('IntendedLearningOutcomeCd')
    module_instance_module_instance = relationship('ModuleInstance')


class ModuleKeyWord(Model):
    __tablename__ = 'module_key_word'
    __table_args__ = {'schema': 'v3'}

    module_key_word_id = Column(Integer, primary_key=True,
                                server_default=text("nextval('v3.module_key_word_module_key_word_id_seq'::regclass)"))
    module_instance_id = Column(ForeignKey('v3.module_instance.module_instance_id', ondelete='CASCADE'), nullable=False)
    module_key_word_text = Column(String(150))

    module_instance = relationship('ModuleInstance')


class ModuleLearningActivity(Model):
    __tablename__ = 'module_learning_activities'
    __table_args__ = {'schema': 'v3'}

    module_instance_module_instance_id = Column(ForeignKey('v3.module_instance.module_instance_id', ondelete='CASCADE'),
                                                primary_key=True, nullable=False)
    learning_activities_category_cd = Column(
        ForeignKey('v3.learning_activities_category.learning_activities_category_cd', ondelete='CASCADE'),
        primary_key=True, nullable=False)
    activity_hours = Column(Numeric)
    learning_activity_description = Column(String(7000))

    learning_activities_category = relationship('LearningActivitiesCategory')
    module_instance_module_instance = relationship('ModuleInstance')


class ModuleLearningResource(Model):
    __tablename__ = 'module_learning_resources'
    __table_args__ = {'schema': 'v3'}

    module_learning_resources_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.module_learning_resources_module_learning_resources_id_seq'::regclass)"))
    module_instance_id = Column(ForeignKey('v3.module_instance.module_instance_id', ondelete='CASCADE'), nullable=False)
    module_learning_resource_type_cd = Column(
        ForeignKey('v3.module_learning_resource_type.module_learning_resource_type_cd', ondelete='CASCADE'),
        nullable=False)
    learning_resource_description = Column(String(7000))

    module_instance = relationship('ModuleInstance')
    module_learning_resource_type = relationship('ModuleLearningResourceType')


class ModuleReferredReassessment(Model):
    __tablename__ = 'module_referred_reassessment'
    __table_args__ = {'schema': 'v3'}

    module_referred_reassessment_id = Column(Numeric, primary_key=True)
    module_instance_module_instance_id = Column(ForeignKey('v3.module_instance.module_instance_id', ondelete='CASCADE'),
                                                nullable=False)
    original_form_of_assessment_type_cd = Column(
        ForeignKey('v3.form_of_assessment_type.form_of_assessment_type_cd', ondelete='CASCADE'), nullable=False)
    referred_reassessment_timescale_id = Column(
        ForeignKey('v3.reassessment_timescale.reassessment_timescale_id', ondelete='CASCADE'), nullable=False)
    referred_form_of_assessment_type_cd = Column(
        ForeignKey('v3.form_of_assessment_type.form_of_assessment_type_cd', ondelete='CASCADE'), nullable=False)
    referred_reassessment_notes = Column(String(550))

    module_instance_module_instance = relationship('ModuleInstance')
    form_of_assessment_type = relationship('FormOfAssessmentType',
                                           primaryjoin='ModuleReferredReassessment.original_form_of_assessment_type_cd == FormOfAssessmentType.form_of_assessment_type_cd')
    form_of_assessment_type1 = relationship('FormOfAssessmentType',
                                            primaryjoin='ModuleReferredReassessment.referred_form_of_assessment_type_cd == FormOfAssessmentType.form_of_assessment_type_cd')
    referred_reassessment_timescale = relationship('ReassessmentTimescale')


class ModuleStaff(Model):
    __tablename__ = 'module_staff'
    __table_args__ = (
        ForeignKeyConstraint(['staff_staff_id', 'staff_email'], ['v3.staff.staff_id', 'v3.staff.staff_email'],
                             ondelete='CASCADE'),
        {'schema': 'v3'}
    )

    module_staff_id = Column(Numeric, primary_key=True)
    staff_staff_id = Column(String(10), nullable=False)
    module_staff_role_module_staff_role_id = Column(
        ForeignKey('v3.module_staff_role.module_staff_role_id', ondelete='CASCADE'), nullable=False)
    module_instance_module_instance_id = Column(ForeignKey('v3.module_instance.module_instance_id', ondelete='CASCADE'),
                                                nullable=False)
    staff_order_in_module = Column(Numeric)
    teaching_delivery_pct = Column(Numeric)
    staff_email = Column(String(150), nullable=False)

    module_instance_module_instance = relationship('ModuleInstance')
    module_staff_role_module_staff_role = relationship('ModuleStaffRole')
    staff_staff = relationship('Staff')


class ModuleTerm(Model):
    __tablename__ = 'module_term'
    __table_args__ = {'schema': 'v3'}

    module_instance_module_instance_id = Column(ForeignKey('v3.module_instance.module_instance_id', ondelete='CASCADE'),
                                                primary_key=True, nullable=False)
    module_term_no = Column(Numeric, primary_key=True, nullable=False)
    module_term_weeks_duration = Column(Numeric)

    module_instance_module_instance = relationship('ModuleInstance')


class Programme(Model):
    __tablename__ = 'programme'
    __table_args__ = (
        UniqueConstraint('programme_root_cd', 'programme_length_cd', 'first_school_cd', 'second_school_cd',
                         'programme_number'),
        {'schema': 'v3'}
    )

    programme_id = Column(Integer, primary_key=True,
                          server_default=text("nextval('v3.programme_programme_id_seq'::regclass)"))
    programme_root_cd = Column(ForeignKey('v3.programme_root_code.programme_root_cd', ondelete='CASCADE'),
                               nullable=False)
    programme_length_cd = Column(ForeignKey('v3.programme_length.programme_length_cd', ondelete='CASCADE'),
                                 nullable=False)
    first_school_cd = Column(ForeignKey('v3.school.school_cd', ondelete='CASCADE'),nullable=False)
    second_school_cd = Column(ForeignKey('v3.school.school_cd', ondelete='CASCADE'),nullable=False)
    programme_number = Column(ForeignKey('v3.programme_number.programme_number', ondelete='CASCADE'), nullable=False)
    benchmark_learning_outcome_id = Column(
        ForeignKey('v3.benchmark_learning_outcome.benchmark_learning_outcome_id', ondelete='CASCADE'))
    programme_status_cd = Column(ForeignKey('v3.programme_status_type.programme_status_type_cd', ondelete='CASCADE'),
                                 nullable=False)
    programme_type_id = Column(ForeignKey('v3.programme_type.programme_type_id', ondelete='CASCADE'), nullable=False)
    programme_submission_id = Column(ForeignKey('v3.programme_submission.programme_submission_id', ondelete='CASCADE'),
                                     nullable=False)
    nfq_level_cd = Column(ForeignKey('v3.nqf_level.nfq_level_cd', ondelete='CASCADE'), nullable=False)
    award_final_award_cd = Column(ForeignKey('v3.award.award_cd', ondelete='CASCADE'), nullable=False)
    programme_variant_type_id = Column(
        ForeignKey('v3.programme_variant_type.programme_variant_type_id', ondelete='CASCADE'), nullable=False)
    variant_description = Column(String(7000))
    other_varient_type = Column(String(50))
    ucas_cd = Column(String(10))
    programme_title = Column(String(150))
    programme_notes = Column(String(7000))
    number_of_stages = Column(Numeric)
    programme_start_date = Column(String(550))
    programme_duration_in_years = Column(Numeric)
    programme_duration_in_months = Column(Numeric)
    programme_delivery_mode_id = Column(
        ForeignKey('v3.programme_delivery_mode.programme_delivery_mode_id', ondelete='CASCADE'), nullable=False)
    programme_additional_funding_id = Column(
        ForeignKey('v3.programme_additional_funding.programme_additional_funding_id', ondelete='CASCADE'),
        nullable=False)
    collaborative_agreement_ind = Column(String(1))
    programme_collaborative_provision_type_id = Column(
        ForeignKey('v3.programme_collaborative_provision_type.programme_collaborative_provision_type_id',
                   ondelete='CASCADE'), nullable=False)
    programme_pgce_funding_type = Column(
        ForeignKey('v3.programme_pgce_funding_type.programme_pgce_funding_type', ondelete='CASCADE'), nullable=False)
    updated_by = Column(String(150))
    programme_standard_fee_ind = Column(String(1))
    updated_on = Column(Date)

    award = relationship('Award')
    benchmark_learning_outcome = relationship('BenchmarkLearningOutcome')
    nqf_level = relationship('NqfLevel')
    programme_additional_funding = relationship('ProgrammeAdditionalFunding')
    programme_collaborative_provision_type = relationship('ProgrammeCollaborativeProvisionType')
    programme_delivery_mode = relationship('ProgrammeDeliveryMode')
    programme_length = relationship('ProgrammeLength')
    programme_number_id = relationship('ProgrammeNumber')
    programme_pgce_funding_id = relationship('ProgrammePgceFundingType')
    programme_root_code = relationship('ProgrammeRootCode')
    programme_status_type = relationship('ProgrammeStatusType')
    programme_submission = relationship('ProgrammeSubmission')
    programme_type = relationship('ProgrammeType')
    programme_variant_type = relationship('ProgrammeVariantType')
    first_school_cd_name = relationship("School", foreign_keys=[first_school_cd])
    second_school_cd_name = relationship("School", foreign_keys=[second_school_cd])


class SitsTier4(Model):
    __tablename__ = 'sits_tier_4'
    __table_args__ = (
        ForeignKeyConstraint(['sub_discipline_sub_discipline_cd', 'sub_discipline_discipline_college_college_cd',
                              'sub_discipline_discipline_discipline_cd'],
                             ['v3.sub_discipline.sub_discipline_cd', 'v3.sub_discipline.discipline_college_college_cd',
                              'v3.sub_discipline.discipline_discipline_cd'], ondelete='CASCADE'),
        {'schema': 'v3'}
    )

    sub_discipline_discipline_college_college_cd = Column(String(10), primary_key=True, nullable=False)
    sub_discipline_discipline_discipline_cd = Column(String(10), primary_key=True, nullable=False)
    sub_discipline_sub_discipline_cd = Column(String(10), primary_key=True, nullable=False)
    sits_tier4_cd = Column(String(10), primary_key=True, nullable=False)
    sits_tier4_name = Column(String(150))

    sub_discipline = relationship('SubDiscipline')


class AdmissionCode(Model):
    __tablename__ = 'admission_code'
    __table_args__ = {'schema': 'v3'}

    admission_code_cd = Column(Numeric, primary_key=True)
    programme_programme_id = Column(ForeignKey('v3.programme.programme_id', ondelete='CASCADE'), nullable=False)
    admission_code_name = Column(String(150))

    programme_programme = relationship('Programme')


class BenchmarkModuleLearningOutcomeUsage(Model):
    __tablename__ = 'benchmark_module_learning_outcome_usage'
    __table_args__ = (
        ForeignKeyConstraint(['module_order_no', 'module_instance_module_instance_id'],
                             ['v3.module_intended_learning_outcomes.module_order_no',
                              'v3.module_intended_learning_outcomes.module_instance_module_instance_id'],
                             ondelete='CASCADE'),
        {'schema': 'v3'}
    )

    benchmark_module_learning_outcome_usage_id = Column(Numeric, primary_key=True)
    benchmark_learning_outcome_measure_id = Column(
        ForeignKey('v3.benchmark_learning_outcome_measure.benchmark_learning_outcome_measure_id', ondelete='CASCADE'),
        nullable=False)
    module_order_no = Column(Numeric, nullable=False)
    module_instance_module_instance_id = Column(Integer, nullable=False)

    benchmark_learning_outcome_measure = relationship('BenchmarkLearningOutcomeMeasure')
    module_intended_learning_outcome = relationship('ModuleIntendedLearningOutcome')


class ModuleIlosAssessed(Model):
    __tablename__ = 'module_ilos_assessed'
    __table_args__ = (
        ForeignKeyConstraint(['module_order_no', 'module_instance_module_instance_id'],
                             ['v3.module_intended_learning_outcomes.module_order_no',
                              'v3.module_intended_learning_outcomes.module_instance_module_instance_id'],
                             ondelete='CASCADE'),
        {'schema': 'v3'}
    )

    module_ilos_assessed_id = Column(Numeric, primary_key=True)
    module_assessment_id = Column(ForeignKey('v3.module_assessment.module_assessment_id', ondelete='CASCADE'),
                                  nullable=False)
    module_order_no = Column(Numeric, nullable=False)
    module_instance_module_instance_id = Column(Integer, nullable=False)

    module_assessment = relationship('ModuleAssessment')
    module_intended_learning_outcome = relationship('ModuleIntendedLearningOutcome')


class ModuleIlosForDeferedReassessment(Model):
    __tablename__ = 'module_ilos_for_defered_reassessment'
    __table_args__ = (
        ForeignKeyConstraint(['module_order_no', 'module_instance_module_instance_id'],
                             ['v3.module_intended_learning_outcomes.module_order_no',
                              'v3.module_intended_learning_outcomes.module_instance_module_instance_id'],
                             ondelete='CASCADE'),
        {'schema': 'v3'}
    )

    module_ilos_deferred_reassessed_id = Column(Numeric, primary_key=True)
    module_deferred_reassessment_id = Column(
        ForeignKey('v3.module_deferred_reassessment.module_deferred_reassessment_id', ondelete='CASCADE'),
        nullable=False)
    module_order_no = Column(Numeric, nullable=False)
    module_instance_module_instance_id = Column(Integer, nullable=False)

    module_deferred_reassessment = relationship('ModuleDeferredReassessment')
    module_intended_learning_outcome = relationship('ModuleIntendedLearningOutcome')


class ModuleIlosForReferredReassessment(Model):
    __tablename__ = 'module_ilos_for_referred_reassessment'
    __table_args__ = (
        ForeignKeyConstraint(['module_order_no', 'module_instance_module_instance_id'],
                             ['v3.module_intended_learning_outcomes.module_order_no',
                              'v3.module_intended_learning_outcomes.module_instance_module_instance_id'],
                             ondelete='CASCADE'),
        {'schema': 'v3'}
    )

    module_ilos_referred_reassessed_id = Column(Numeric, primary_key=True)
    module_referred_reassessment_id = Column(
        ForeignKey('v3.module_referred_reassessment.module_referred_reassessment_id', ondelete='CASCADE'),
        nullable=False)
    module_order_no = Column(Numeric, nullable=False)
    module_instance_module_instance_id = Column(Integer, nullable=False)

    module_intended_learning_outcome = relationship('ModuleIntendedLearningOutcome')
    module_referred_reassessment = relationship('ModuleReferredReassessment')


class ProgrammeCampus(Model):
    __tablename__ = 'programme_campus'
    __table_args__ = {'schema': 'v3'}

    programme_campus_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_campus_programme_campus_id_seq'::regclass)"))
    campus_campus_cd = Column(ForeignKey('v3.campus.campus_cd', ondelete='CASCADE'), nullable=False)
    programme_programme_id = Column(ForeignKey('v3.programme.programme_id', ondelete='CASCADE'), nullable=False)

    campus = relationship('Campus')
    programme_programme = relationship('Programme')


class ProgrammeCollege(Model):
    __tablename__ = 'programme_college'
    __table_args__ = {'schema': 'v3'}

    programme_programme_id = Column(ForeignKey('v3.programme.programme_id', ondelete='CASCADE'), primary_key=True,
                                    nullable=False)
    college_college_cd = Column(ForeignKey('v3.college.college_cd', ondelete='CASCADE'), primary_key=True,
                                nullable=False)
    programme_college_seq = Column(Numeric, primary_key=True, nullable=False)

    college = relationship('College')
    programme_programme = relationship('Programme')


class ProgrammeDiscipline(Model):
    __tablename__ = 'programme_discipline'
    __table_args__ = {'schema': 'v3'}

    programme_programme_id = Column(ForeignKey('v3.programme.programme_id', ondelete='CASCADE'), primary_key=True,
                                    nullable=False)
    discipline_id = Column(ForeignKey('v3.discipline.discipline_id', ondelete='CASCADE'), nullable=False)
    discipline_cd = Column(String(10), primary_key=True, nullable=False)
    programme_discipline_seq = Column(Numeric, primary_key=True, nullable=False)
    programme_discipline_percentage = Column(Numeric)

    discipline = relationship('Discipline')
    programme_programme = relationship('Programme')


class ProgrammeEntryMonth(Model):
    __tablename__ = 'programme_entry_month'
    __table_args__ = (
        UniqueConstraint('programme_id', 'month'),
        {'schema': 'v3'}
    )

    programme_entry_month_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_entry_month_programme_entry_month_id_seq'::regclass)"))
    programme_id = Column(ForeignKey('v3.programme.programme_id', ondelete='CASCADE'), nullable=False)
    month = Column(String(10))

    programme = relationship('Programme')


class ProgrammeInstance(Model):
    __tablename__ = 'programme_instance'
    __table_args__ = (
        UniqueConstraint('programme_programme_id', 'academic_year_id'),
        {'schema': 'v3'}
    )

    programme_instance_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_instance_programme_instance_id_seq'::regclass)"))
    programme_programme_id = Column(ForeignKey('v3.programme.programme_id', ondelete='CASCADE'), nullable=False)
    academic_year_id = Column(ForeignKey('v3.academic_year.academic_year_id', ondelete='CASCADE'), nullable=False)
    programme_instance_status_cd = Column(
        ForeignKey('v3.programme_status_type.programme_status_type_cd', ondelete='CASCADE'), nullable=False)
    pathway_type_id = Column(ForeignKey('v3.pathway_type.pathway_type_id', ondelete='CASCADE'), nullable=False)
    admission_application_type_id = Column(
        ForeignKey('v3.admission_application_type.admission_application_type_id', ondelete='CASCADE'), nullable=False)
    programme_progression_type_id = Column(
        ForeignKey('v3.programme_progression_type.programme_progression_type_id', ondelete='CASCADE'), nullable=False)
    sandwich_course_type_id = Column(ForeignKey('v3.sandwich_course_type.sandwich_course_type_id', ondelete='CASCADE'))
    course_delivery_initiative_id = Column(
        ForeignKey('v3.course_delivery_initiative.course_delivery_initiative_id', ondelete='CASCADE'))
    application_procedure_type_id = Column(
        ForeignKey('v3.application_procedure_type.application_procedure_type_id', ondelete='CASCADE'), nullable=False)
    academic_description = Column(String(7000))
    marketing_description = Column(String(7000))
    abstract_text = Column(String(550))
    educational_aims_description = Column(String(7000))
    programme_structure_description = Column(String(7000))
    programme_structure_additonal_description = Column(String(7000))
    programme_modules_description = Column(String(7000))
    programme_module_structure_description = Column(String(7000))
    url_for_module_information = Column(String(150))
    programme_instance_start_date = Column(Date)
    classification_description = Column(String(7000))
    marketing_employability_text = Column(String(7000))
    critical_success_factor_description = Column(String(7000))
    teacher_training_course_type_id = Column(
        ForeignKey('v3.teacher_training_course_type.teacher_training_course_type_id', ondelete='CASCADE'))
    marketing_learning_and_teaching_activty_description = Column(String(7000))
    marketing_assessment_methods_description = Column(String(7000))
    college_support_for_learning = Column(String(7000))
    university_support_for_learning = Column(String(7000))
    programme_specific_award_rules = Column(String(7000))
    pathway_names = Column(String(7000))
    student_additional_expenses = Column(String(7000))
    programme_delivery_characteristics_description = Column(String(7000))
    mcr_code = Column(String(10))
    ofs_internal_finance_code = Column(String(150))
    hesa_information_reposnsibility_ind = Column(String(1))
    unistats_programme_ind = Column(String(1))
    closed_course_ind = Column(String(1))
    other_application_type_description = Column(String(7000))
    pg_fast_track_application_ind = Column(String(1))
    entry_requirement_description = Column(String(7000))
    contextual_offer_support_description = Column(String(7000))
    non_academic_requirements_description = Column(String(7000))
    exceptional_selection_description = Column(String(7000))
    dbs_check_ind = Column(String(1))
    dbs_check_level_id = Column(ForeignKey('v3.dbs_check_level.dbs_check_level_id', ondelete='CASCADE'), nullable=False)
    updated_by = Column(String(150))
    updated_dt = Column(Date)

    academic_year = relationship('AcademicYear')
    admission_application_type = relationship('AdmissionApplicationType')
    application_procedure_type = relationship('ApplicationProcedureType')
    course_delivery_initiative = relationship('CourseDeliveryInitiative')
    dbs_check_level = relationship('DbsCheckLevel')
    pathway_type = relationship('PathwayType')
    programme_status_type = relationship('ProgrammeStatusType')
    programme_programme = relationship('Programme')
    programme_progression_type = relationship('ProgrammeProgressionType')
    sandwich_course_type = relationship('SandwichCourseType')
    teacher_training_course_type = relationship('TeacherTrainingCourseType')


class ProgrammeKeyWord(Model):
    __tablename__ = 'programme_key_word'
    __table_args__ = {'schema': 'v3'}

    programme_key_word_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_key_word_programme_key_word_id_seq'::regclass)"))
    programme_id = Column(ForeignKey('v3.programme.programme_id', ondelete='CASCADE'), nullable=False)
    programme_key_word_text = Column(String(150))

    programme = relationship('Programme')


class ProgrammeNonStandardFee(Model):
    __tablename__ = 'programme_non_standard_fee'
    __table_args__ = {'schema': 'v3'}

    programme_non_standard_fee_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_non_standard_fee_programme_non_standard_fee_id_seq'::regclass)"))
    programme_id = Column(ForeignKey('v3.programme.programme_id', ondelete='CASCADE'), nullable=False)
    fee_student_type_id = Column(ForeignKey('v3.fee_student_type.fee_student_type_id', ondelete='CASCADE'),
                                 nullable=False)
    programme_non_standard_fee_value = Column(Numeric)

    fee_student_type = relationship('FeeStudentType')
    programme = relationship('Programme')


class ProgrammePartnerInstitution(Model):
    __tablename__ = 'programme_partner_institution'
    __table_args__ = {'schema': 'v3'}

    programme_partner_institution_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_partner_institution_programme_partner_institution_seq'::regclass)"))
    programme_id = Column(ForeignKey('v3.programme.programme_id', ondelete='CASCADE'), nullable=False)
    partner_institution_cd = Column(ForeignKey('v3.partner_institution.partner_institution_cd', ondelete='CASCADE'),
                                    nullable=False)

    partner_institution = relationship('PartnerInstitution')
    programme = relationship('Programme')


class ProgrammeReportingAttribute(Model):
    __tablename__ = 'programme_reporting_attribute'
    __table_args__ = {'schema': 'v3'}

    programme_reporting_attribute_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_reporting_attribute_programme_reporting_attribute_seq'::regclass)"))
    programme_programme_id = Column(ForeignKey('v3.programme.programme_id', ondelete='CASCADE'), nullable=False)
    reporting_attribute_id = Column(ForeignKey('v3.reporting_attribute.reporting_attribute_id', ondelete='CASCADE'),
                                    nullable=False)

    programme_programme = relationship('Programme')
    reporting_attribute = relationship('ReportingAttribute')


class ProgrammeStudyMode(Model):
    __tablename__ = 'programme_study_mode'
    __table_args__ = {'schema': 'v3'}

    programme_study_mode_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_study_mode_programme_study_mode_id_seq'::regclass)"))
    study_mode_study_mode_cd = Column(ForeignKey('v3.study_mode.study_mode_cd', ondelete='CASCADE'), nullable=False)
    programme_id = Column(ForeignKey('v3.programme.programme_id', ondelete='CASCADE'), nullable=False)

    programme = relationship('Programme')
    study_mode = relationship('StudyMode')


class RelatedProgramme(Model):
    __tablename__ = 'related_programme'
    __table_args__ = {'schema': 'v3'}

    related_programme_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.related_programme_related_programme_id_seq'::regclass)"))
    first_related_programme_id = Column(ForeignKey('v3.programme.programme_id', ondelete='CASCADE'), nullable=False)
    second_related_programme_id = Column(ForeignKey('v3.programme.programme_id', ondelete='CASCADE'), nullable=False)

    first_related_programme = relationship('Programme',
                                           primaryjoin='RelatedProgramme.first_related_programme_id == Programme.programme_id')
    second_related_programme = relationship('Programme',
                                            primaryjoin='RelatedProgramme.second_related_programme_id == Programme.programme_id')


class AnticipatedProgrammeStudentNumber(Model):
    __tablename__ = 'anticipated_programme_student_number'
    __table_args__ = {'schema': 'v3'}

    anticipated_program_student_numbers_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.anticipated_programme_student_anticipated_program_student_n_seq'::regclass)"))
    programme_instance_id = Column(ForeignKey('v3.programme_instance.programme_instance_id', ondelete='CASCADE'),
                                   nullable=False)
    anticipated_student_number_type_id = Column(
        ForeignKey('v3.anticipated_student_number_type.anticipated_student_number_type_id', ondelete='CASCADE'),
        nullable=False)
    anticipated_student_number = Column(Numeric)

    anticipated_student_number_type = relationship('AnticipatedStudentNumberType')
    programme_instance = relationship('ProgrammeInstance')


class EducationalLearningOutcome(Model):
    __tablename__ = 'educational_learning_outcomes'
    __table_args__ = {'schema': 'v3'}

    programme_programme_id = Column(ForeignKey('v3.programme_instance.programme_instance_id', ondelete='CASCADE'),
                                    primary_key=True, nullable=False)
    educational_learning_outcome_order_no = Column(Numeric, primary_key=True, nullable=False)
    learning_outcome_description = Column(String(7000))

    programme_programme = relationship('ProgrammeInstance')


class ProgrammeAccreditation(Model):
    __tablename__ = 'programme_accreditation'
    __table_args__ = {'schema': 'v3'}

    programme_accreditation_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_accreditation_programme_accreditation_id_seq'::regclass)"))
    programme_instance_id = Column(ForeignKey('v3.programme_instance.programme_instance_id', ondelete='CASCADE'),
                                   nullable=False)
    programme_accreditation_body_code = Column(
        ForeignKey('v3.programme_accreditation_body.programme_accreditation_body_code', ondelete='CASCADE'),
        nullable=False)
    programme_accreditation_type_code = Column(
        ForeignKey('v3.programme_accreditation_type.programme_accreditation_type_code', ondelete='CASCADE'),
        nullable=False)
    student_choice_ind = Column(String(1))
    accreditation_start_date = Column(Date)
    expected_accreditation_end_date = Column(Date)
    actual_accreditation_end_date = Column(Date)
    accreditation_renewal_date = Column(Date)
    accreditation_status_description = Column(String(7000))
    accreditation_report_recieved_date = Column(Date)

    programme_accreditation_body = relationship('ProgrammeAccreditationBody')
    programme_accreditation_type = relationship('ProgrammeAccreditationType')
    programme_instance = relationship('ProgrammeInstance')


class ProgrammeAdministrationNote(Model):
    __tablename__ = 'programme_administration_note'
    __table_args__ = {'schema': 'v3'}

    programme_administration_note_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_administration_note_programme_administration_note_seq'::regclass)"))
    programme_instance_id = Column(ForeignKey('v3.programme_instance.programme_instance_id', ondelete='CASCADE'),
                                   nullable=False)
    programme_administration_note_type_id = Column(
        ForeignKey('v3.administration_note_type.programme_administration_note_type_id', ondelete='CASCADE'),
        nullable=False)
    note_date = Column(Date)
    note_name = Column(String(150))
    note_text = Column(String(7000))

    programme_administration_note_type = relationship('AdministrationNoteType')
    programme_instance = relationship('ProgrammeInstance')


class ProgrammeContact(Model):
    __tablename__ = 'programme_contact'
    __table_args__ = (
        ForeignKeyConstraint(['staff_id', 'staff_email'], ['v3.staff.staff_id', 'v3.staff.staff_email'],
                             ondelete='CASCADE'),
        {'schema': 'v3'}
    )

    programme_contact_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_contact_programme_contact_id_seq'::regclass)"))
    programme_instance_id = Column(ForeignKey('v3.programme_instance.programme_instance_id', ondelete='CASCADE'),
                                   nullable=False)
    staff_id = Column(String(10), nullable=False)
    prgoramme_contact_type_id = Column(
        ForeignKey('v3.programme_contact_type.prgoramme_contact_type_id', ondelete='CASCADE'), nullable=False)
    staff_email = Column(String(150), nullable=False)

    prgoramme_contact_type = relationship('ProgrammeContactType')
    programme_instance = relationship('ProgrammeInstance')
    staff = relationship('Staff')


class ProgrammeHecosCode(Model):
    __tablename__ = 'programme_hecos_code'
    __table_args__ = (
        UniqueConstraint('programme_instance_id', 'programme_hecos_code', 'programme_hecos_code_seq'),
        {'schema': 'v3'}
    )

    programme_hecos_code_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_hecos_code_programme_hecos_code_id_seq'::regclass)"))
    programme_instance_id = Column(ForeignKey('v3.programme_instance.programme_instance_id', ondelete='CASCADE'),
                                   nullable=False)
    programme_hecos_code = Column(String(150))
    programme_hecos_code_seq = Column(Numeric)
    programme_hecos_code_split = Column(String(150))
    programme_hefce_price_group = Column(String(150))

    programme_instance = relationship('ProgrammeInstance')


class ProgrammeLearningOutcomeArea(Model):
    __tablename__ = 'programme_learning_outcome_areas'
    __table_args__ = {'schema': 'v3'}

    programme_learning_outcome_area_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_learning_outcome_ar_programme_learning_outcome_ar_seq'::regclass)"))
    learning_and_teaching_activity_description = Column(String(7000))
    programme_instance_id = Column(ForeignKey('v3.programme_instance.programme_instance_id', ondelete='CASCADE'),
                                   nullable=False)
    programme_learning_outcome_type_cd = Column(
        ForeignKey('v3.programme_learning_outcome_type.programme_learning_outcome_type_cd', ondelete='CASCADE'),
        nullable=False)

    programme_instance = relationship('ProgrammeInstance')
    programme_learning_outcome_type = relationship('ProgrammeLearningOutcomeType')


class ProgrammePsrb(Model):
    __tablename__ = 'programme_psrb'
    __table_args__ = {'schema': 'v3'}

    programme_psrb_id = Column(Integer, primary_key=True,
                               server_default=text("nextval('v3.programme_psrb_programme_psrb_id_seq'::regclass)"))
    programme_instance_id = Column(ForeignKey('v3.programme_instance.programme_instance_id', ondelete='CASCADE'),
                                   nullable=False)
    programme_psrb_type_id = Column(ForeignKey('v3.programme_psrb_type.programme_psrb_type_id', ondelete='CASCADE'),
                                    nullable=False)
    psrb_predicted_start_date = Column(Date)

    programme_instance = relationship('ProgrammeInstance')
    programme_psrb_type = relationship('ProgrammePsrbType')


class ProgrammeStage(Model):
    __tablename__ = 'programme_stage'
    __table_args__ = {'schema': 'v3'}

    programme_programme_id = Column(ForeignKey('v3.programme_instance.programme_instance_id', ondelete='CASCADE'),
                                    primary_key=True, nullable=False)
    programme_stage_no = Column(String(10), primary_key=True, nullable=False)
    programme_stage_overview = Column(String(7000))
    stage_overview_description = Column(String(7000))
    programme_specific_progression_rules_description = Column(String(7000))

    programme_programme = relationship('ProgrammeInstance')


class CohortProgramme(Model):
    __tablename__ = 'cohort_programme'
    __table_args__ = (
        ForeignKeyConstraint(['programme_stage_programme_stage_no', 'programme_stage_programme_programme_id'],
                             ['v3.programme_stage.programme_stage_no', 'v3.programme_stage.programme_programme_id'],
                             ondelete='CASCADE'),
        {'schema': 'v3'}
    )

    cohort_programme_id = Column(Numeric, primary_key=True)
    student_cohort_student_cohort_id = Column(ForeignKey('v3.student_cohort.student_cohort_id', ondelete='CASCADE'),
                                              nullable=False)
    programme_stage_programme_stage_no = Column(String(10), nullable=False)
    programme_stage_programme_programme_id = Column(Integer, nullable=False)
    admission_entry_requirements_description = Column(String(7000))
    admission_required_subjects_description = Column(String(7000))
    admission_selection_criteria = Column(String(7000))
    application_procedure_description = Column(String(7000))
    admission_criteria_description = Column(String(7000))

    programme_stage = relationship('ProgrammeStage')
    student_cohort_student_cohort = relationship('StudentCohort')


class IndustrialPlacementElement(Model):
    __tablename__ = 'industrial_placement_element'
    __table_args__ = (
        ForeignKeyConstraint(['programme_stage_programme_stage_no', 'programme_stage_programme_programme_id'],
                             ['v3.programme_stage.programme_stage_no', 'v3.programme_stage.programme_programme_id'],
                             ondelete='CASCADE'),
        {'schema': 'v3'}
    )

    industrial_placement_element_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.industrial_placement_element_industrial_placement_element_i_seq'::regclass)"))
    programme_stage_programme_stage_no = Column(String(10), nullable=False)
    programme_stage_programme_programme_id = Column(Integer, nullable=False)
    length_industrial_placement_months = Column(Numeric)
    further_information_description = Column(String(7000))
    paid_industrial_placement_ind = Column(String(1))

    programme_stage = relationship('ProgrammeStage')


class ProgrammeAccreditationVisit(Model):
    __tablename__ = 'programme_accreditation_visit'
    __table_args__ = {'schema': 'v3'}

    programme_accreditation_programme_accreditation_id = Column(
        ForeignKey('v3.programme_accreditation.programme_accreditation_id', ondelete='CASCADE'), primary_key=True,
        nullable=False,
        server_default=text("nextval('v3.programme_accreditation_visit_programme_accreditation_progr_seq'::regclass)"))
    accreditation_visit_date = Column(Date, primary_key=True, nullable=False)
    accreditation_visit_description = Column(String(7000))

    programme_accreditation_programme_accreditation = relationship('ProgrammeAccreditation')


class ProgrammeLearningOutcome(Model):
    __tablename__ = 'programme_learning_outcome'
    __table_args__ = {'schema': 'v3'}

    programme_learning_outcome_area_id = Column(
        ForeignKey('v3.programme_learning_outcome_areas.programme_learning_outcome_area_id', ondelete='CASCADE'),
        primary_key=True, nullable=False)
    programme_learning_outcome_order_no = Column(Numeric, primary_key=True, nullable=False)
    learning_outcome_description = Column(String(7000))

    programme_learning_outcome_area = relationship('ProgrammeLearningOutcomeArea')


class ProgrammeStageModule(Model):
    __tablename__ = 'programme_stage_module'
    __table_args__ = (
        ForeignKeyConstraint(['programme_stage_no', 'programme_programme_id'],
                             ['v3.programme_stage.programme_stage_no', 'v3.programme_stage.programme_programme_id'],
                             ondelete='CASCADE'),
        UniqueConstraint('programme_stage_no', 'programme_programme_id', 'module_instance_id'),
        {'schema': 'v3'}
    )

    programme_stage_module_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_stage_module_programme_stage_module_id_seq'::regclass)"))
    programme_stage_no = Column(String(10), nullable=False)
    programme_programme_id = Column(Integer, nullable=False)
    module_instance_id = Column(ForeignKey('v3.module_instance.module_instance_id', ondelete='CASCADE'))
    compulsory_optional_ind = Column(String(1))
    module_notes = Column(String(7000))
    non_condonable_ind = Column(String(1))

    module_instance = relationship('ModuleInstance')
    programme_stage = relationship('ProgrammeStage')


class StudyAbroadElement(Model):
    __tablename__ = 'study_abroad_element'
    __table_args__ = (
        ForeignKeyConstraint(['programme_stage_programme_stage_no', 'programme_stage_programme_programme_id'],
                             ['v3.programme_stage.programme_stage_no', 'v3.programme_stage.programme_programme_id'],
                             ondelete='CASCADE'),
        {'schema': 'v3'}
    )

    study_abroad_element_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.study_abroad_element_study_abroad_element_id_seq'::regclass)"))
    programme_stage_programme_stage_no = Column(String(10), nullable=False)
    programme_stage_programme_programme_id = Column(Integer, nullable=False)
    length_study_abroad_months = Column(Numeric)
    paid_work_experience_ind = Column(String(1))
    further_information_description = Column(String(7000))

    programme_stage = relationship('ProgrammeStage')


class BenchmarkProgrammeLearningOutcomeUsage(Model):
    __tablename__ = 'benchmark_programme_learning_outcome_usage'
    __table_args__ = (
        ForeignKeyConstraint(['programme_learning_outcome_order_no', 'programme_learning_outcome_area_id'],
                             ['v3.programme_learning_outcome.programme_learning_outcome_order_no',
                              'v3.programme_learning_outcome.programme_learning_outcome_area_id'], ondelete='CASCADE'),
        {'schema': 'v3'}
    )

    benchmark_programme_learning_outcome_usage_id = Column(Numeric, primary_key=True)
    programme_learning_outcome_order_no = Column(Numeric, nullable=False)
    programme_learning_outcome_area_id = Column(Integer, nullable=False)
    benchmark_learning_outcome_measure_id = Column(
        ForeignKey('v3.benchmark_learning_outcome_measure.benchmark_learning_outcome_measure_id', ondelete='CASCADE'),
        nullable=False)

    benchmark_learning_outcome_measure = relationship('BenchmarkLearningOutcomeMeasure')
    programme_learning_outcome = relationship('ProgrammeLearningOutcome')


class ProgrammeIloAssessmentMethod(Model):
    __tablename__ = 'programme_ilo_assessment_method'
    __table_args__ = (
        ForeignKeyConstraint(['programme_learning_outcome_order_no', 'programme_learning_outcome_area_id'],
                             ['v3.programme_learning_outcome.programme_learning_outcome_order_no',
                              'v3.programme_learning_outcome.programme_learning_outcome_area_id'], ondelete='CASCADE'),
        {'schema': 'v3'}
    )

    programme_ilo_assessment_method_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_ilo_assessment_meth_programme_ilo_assessment_meth_seq'::regclass)"))
    assessment_method_description = Column(String(7000))
    programme_learning_outcome_order_no = Column(Numeric, nullable=False)
    programme_learning_outcome_area_id = Column(Integer, nullable=False)

    programme_learning_outcome = relationship('ProgrammeLearningOutcome')


class ProgrammeModuleLearningOutcomeUsage(Model):
    __tablename__ = 'programme_module_learning_outcome_usage'
    __table_args__ = (
        ForeignKeyConstraint(['module_order_no', 'module_instance_module_instance_id'],
                             ['v3.module_intended_learning_outcomes.module_order_no',
                              'v3.module_intended_learning_outcomes.module_instance_module_instance_id'],
                             ondelete='CASCADE'),
        ForeignKeyConstraint(['programme_learning_outcome_order_no', 'programme_learning_outcome_area_id'],
                             ['v3.programme_learning_outcome.programme_learning_outcome_order_no',
                              'v3.programme_learning_outcome.programme_learning_outcome_area_id'], ondelete='CASCADE'),
        {'schema': 'v3'}
    )

    programme_module_learning_outcome_usage_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_module_learning_out_programme_module_learning_out_seq'::regclass)"))
    programme_learning_outcome_order_no = Column(Numeric, nullable=False)
    programme_learning_outcome_area_id = Column(Integer, nullable=False)
    module_order_no = Column(Numeric, nullable=False)
    module_instance_module_instance_id = Column(Integer, nullable=False)

    module_intended_learning_outcome = relationship('ModuleIntendedLearningOutcome')
    programme_learning_outcome = relationship('ProgrammeLearningOutcome')


class ProgrammeStageModuleInstanceGroup(Model):
    __tablename__ = 'programme_stage_module_instance_group'
    __table_args__ = {'schema': 'v3'}

    prgoramme_stage_module_instance_group_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('v3.programme_stage_module_instan_prgoramme_stage_module_instan_seq'::regclass)"))
    programme_stage_module_id = Column(
        ForeignKey('v3.programme_stage_module.programme_stage_module_id', ondelete='CASCADE'), nullable=False)
    module_group_id = Column(ForeignKey('v3.module_instance_group.module_group_id', ondelete='CASCADE'), nullable=False)
    required_credits_for_group = Column(Numeric)

    module_group = relationship('ModuleInstanceGroup')
    programme_stage_module = relationship('ProgrammeStageModule')
