# Code pour diagrammes UML
## Cas d'utilisation

@startuml
left to right direction
skinparam packageStyle rectangle

actor "Utilisateur" as U
actor "Admin" as A
actor "Collaborateur" as Collab
actor "Client" as C
actor "API SNCF" as SNCF

' Héritage des acteurs selon ton schéma
U <|-- C
U <|-- Collab
U <|-- A

rectangle "Système Backend Transport Ferroviaire" {

  usecase "S'inscrire / Se connecter" as UC_Auth
  usecase "Affecter un rôle" as UC_AssignRole
  usecase "Gérer les rôles (hors Admin)" as UC_ManageRoles
  
  usecase "Rechercher des trajets (Autocomplétion)" as UC_Search
  usecase "Voir détail tarif / Réduction abonnement" as UC_Tariff
  usecase "Réserver / Payer un billet" as UC_Book
  
  usecase "Gérer les lignes & gares" as UC_ManageLines
  usecase "Planifier / Modifier / Supprimer un trajet" as UC_ManageTrips
  
  usecase "Récupérer gares & temps de trajet" as UC_SNCF_Sync
}

' Relations
U --> UC_Auth

A --> UC_AssignRole
A --> UC_ManageRoles

C --> UC_Search
C --> UC_Tariff
C --> UC_Book

Collab --> UC_ManageLines
Collab --> UC_ManageTrips

UC_Auth --> A
UC_Auth --> Collab
UC_Auth --> C

' Inclusions avec l'API SNCF
UC_ManageLines .> UC_SNCF_Sync : <<include>>
UC_ManageTrips .> UC_SNCF_Sync : <<include>>
UC_Search .> UC_SNCF_Sync : <<include>>

UC_SNCF_Sync <--> SNCF

@enduml


## Classes

@startuml

enum Role {
  CLIENT
  COLLABORATEUR
  ADMIN
}

enum BookingStatus {
  PAYE
  ANNULE
  EN ATTENTE DE PAIEMENT
}

class User {
  + id : Integer
  + username : String
  + email : String
  + passwordHash : String
  + role : Role
  + subscriptionId : Integer
  + register()
  + login()
}

class Subscription {
  + id : Integer
  + name : String
  + discountPercentage : Float
  + conditions : String
}

class Station {
  + id : Integer
  + codeGareSNCF : String
  + name : String
  + city : String
}

class StationAdjacency {
  + id : Integer
  + station1Id : Integer
  + station2Id : Integer
  + railType : String
}

class OperatingLine {
  + id : Integer
  + code : String
  + departureStationId : Integer
  + arrivalStationId : Integer
  + estimatedDurationMinutes : Integer
}

class Trip {
  + id : Integer
  + lineId : Integer
  + departureTime : DateTime
  + arrivalTime : DateTime
  + totalSeats : Integer
  + availableSeats : Integer
  + basePrice : Float
}

class Booking {
  + id : Integer
  + userId : Integer
  + tripId : Integer
  + status : BookingStatus
  + finalPrice : Float
  + createdAt : DateTime
  + cancel()
}

' Relations
User "0..*" -- "0..1" Subscription : souscrit à >
User "1" -- "0..*" Booking : passe >
Booking "0..*" -- "1" Trip : concerne >
Trip "0..*" -- "1" OperatingLine : s'exécute sur >
OperatingLine "1" -- "2" Station : relie >
StationAdjacency "0..*" -- "2" Station : connecte >

@enduml

## Structure

@startuml
skinparam componentStyle uml2
skinparam linetype ortho
left to right direction

package "Frontend (Webmasters)" {
  [Interface Utilisateur Web] as UI
}

package "Backend - API REST" {
  
  package "Couche Controller (REST)" {
    [AuthController] as C_Auth
    [LineController] as C_Line
    [TripController] as C_Trip
    [BookingController] as C_Book
  }
  
  package "Couche Service (Métier)" {
    [AuthService] as S_Auth
    [LineService] as S_Line
    [TripService] as S_Trip
    [BookingService] as S_Book
    [SNCFClientService] as S_SNCF
  }
  
  package "Couche DAO / Repository" {
    [UserRepository] as D_User
    [LineRepository] as D_Line
    [StationRepository] as D_Station
    [TripRepository] as D_Trip
    [BookingRepository] as D_Book
  }
}

database "PostgreSQL" as BDD
cloud "API SNCF Externe" as ExtSNCF

C_Auth -[hidden]down-> C_Line
C_Line -[hidden]down-> C_Trip
C_Trip -[hidden]down-> C_Book

S_Auth -[hidden]down-> S_Line
S_Line -[hidden]down-> S_Trip
S_Trip -[hidden]down-> S_Book
S_Book -[hidden]down-> S_SNCF

D_User -[hidden]down-> D_Line
D_Line -[hidden]down-> D_Station
D_Station -[hidden]down-> D_Trip
D_Trip -[hidden]down-> D_Book

"Couche Controller (REST)" -[hidden]right-> "Couche Service (Métier)"
"Couche Service (Métier)" -[hidden]right-> "Couche DAO / Repository"

' Flux Frontend -> Controller
UI --> C_Auth
UI --> C_Line
UI --> C_Trip
UI --> C_Book

' Flux Controller -> Service
C_Auth --> S_Auth
C_Line --> S_Line
C_Trip --> S_Trip
C_Book --> S_Book

' Flux Service -> DAO (Lignes alignées)
S_Auth --> D_User
S_Line --> D_Line
S_Line --> D_Station
S_Trip --> D_Trip
S_Trip --> D_Station
S_Book --> D_Book
S_Book --> D_Trip
S_Book --> D_User

' Interfaçage API SNCF
S_Line ..> S_SNCF
S_Trip ..> S_SNCF
S_SNCF ..> ExtSNCF : HTTP / REST

' Flux DAO -> BDD
D_User --> BDD
D_Line --> BDD
D_Station --> BDD
D_Trip --> BDD
D_Book --> BDD

@enduml
