@startuml
class Project {
  - id: Integer
  - name: String
  - description: String
  - stakeholder: ManyToMany<Organization>
  - team_member: ManyToMany<User>
}

class Participant {
  - id: Integer
  - project: ForeignKey<Project>
  - participant_id: String
  - gender: String
  - date_of_birth: Date
  - race: String
  - marital_status: String
  - language: String
}

Project "1" -- "*" Participant : Contains

class Organization {
  // like University or research institution
}

class Researchers {
  // who has the permission to use the data
}
@enduml