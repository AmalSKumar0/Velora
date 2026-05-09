# Database Schema and ER Diagram

## 1. Chen's Notation ER Diagram
Based on the provided classical ER diagram symbols:
*   **Rectangles**: Entities
*   **Ellipses**: Attributes
*   **Diamonds**: Relationships
*   **Lines**: Links

*Note: Due to the scale of the database, this diagram highlights the core relationships. A complete relational schema is provided in section 2.*

```mermaid
flowchart TD
    %% Entities (Rectangles)
    User[User]
    ArtistProfile[ArtistProfile]
    Request[Request]
    Proposal[Proposal]
    Order[Order]
    Payment[Payment]

    %% Relationships (Diamonds)
    User_Artist{has}
    User_Request{creates}
    Artist_Prop{submits}
    Req_Prop{receives}
    Prop_Order{becomes}
    Order_Pay{has}

    %% Connect Entities to Relationships (Lines)
    User --- User_Artist --- ArtistProfile
    User --- User_Request --- Request
    ArtistProfile --- Artist_Prop --- Proposal
    Request --- Req_Prop --- Proposal
    Proposal --- Prop_Order --- Order
    Order --- Order_Pay --- Payment

    %% Attributes (Ellipses)
    %% User Attributes
    u_id([id])
    u_role([role])
    u_bio([bio])
    User --- u_id
    User --- u_role
    User --- u_bio

    %% ArtistProfile Attributes
    ap_id([id])
    ap_name([display_name])
    ArtistProfile --- ap_id
    ArtistProfile --- ap_name

    %% Request Attributes
    r_id([id])
    r_title([title])
    r_status([status])
    Request --- r_id
    Request --- r_title
    Request --- r_status

    %% Proposal Attributes
    p_id([id])
    p_price([price])
    Proposal --- p_id
    Proposal --- p_price

    %% Order Attributes
    o_id([id])
    o_amt([amount])
    o_stat([status])
    Order --- o_id
    Order --- o_amt
    Order --- o_stat

    %% Payment Attributes
    pay_id([id])
    pay_stat([status])
    Payment --- pay_id
    Payment --- pay_stat
```

## 2. Complete Relational Database Schema
This diagram uses standard Crow's Foot notation to illustrate all tables, columns, foreign keys, and cardinalities in the system.

```mermaid
erDiagram
    USER ||--o| ARTIST_PROFILE : "has_profile"
    USER ||--o{ REQUEST : "creates"
    USER ||--o{ ORDER : "places"
    USER ||--o{ REVIEW : "writes"
    USER ||--o{ DISPUTE : "raises"
    
    ARTIST_PROFILE ||--o{ PORTFOLIO_ITEM : "showcases"
    ARTIST_PROFILE ||--o{ PROPOSAL : "submits"
    ARTIST_PROFILE ||--o{ ORDER : "fulfills"
    
    REQUEST ||--o{ REQUEST_IMAGE : "contains"
    REQUEST ||--o{ PROPOSAL : "receives"
    
    PROPOSAL ||--|{ ORDER : "converted_to"
    
    ORDER ||--o| PAYMENT : "requires"
    ORDER ||--o{ SUBMISSION : "has"
    ORDER ||--o| REVIEW : "receives"
    ORDER ||--o{ DISPUTE : "involves"
    
    SUBMISSION ||--o{ SUBMISSION_REVIEW : "undergoes"
    SUBMISSION ||--o{ ORDER_UPDATE : "associated_with"
    
    TAG }o--o{ ARTIST_PROFILE : "categorizes"
    TAG }o--o{ PORTFOLIO_ITEM : "describes"
    TAG }o--o{ REQUEST : "tags"

    USER {
        UUID id PK
        string username
        string role
        string bio
        string profile_image
        datetime created_at
    }

    ARTIST_PROFILE {
        UUID id PK
        UUID user_id FK
        string display_name
        string bio
        string portfolioURL
        boolean is_available
        datetime created_at
    }

    PORTFOLIO_ITEM {
        UUID id PK
        UUID artist_id FK
        string title
        string image
        datetime created_at
    }

    TAG {
        int id PK
        string name
    }

    REQUEST {
        UUID id PK
        UUID client_id FK
        string title
        text description
        int budget_min
        int budget_max
        string status
        datetime created_at
    }

    REQUEST_IMAGE {
        UUID id PK
        UUID request_id FK
        string image
    }

    PROPOSAL {
        UUID id PK
        UUID request_id FK
        UUID artist_id FK
        int price
        text message
        int delivery_days
        string status
        datetime created_at
    }

    ORDER {
        UUID id PK
        UUID request_id FK
        UUID proposal_id FK
        UUID client_id FK
        UUID artist_id FK
        int amount
        string status
        int revision_count
        datetime created_at
        datetime updated_at
    }

    SUBMISSION {
        UUID id PK
        UUID order_id FK
        int version
        string preview_file
        string original_file
        datetime created_at
    }

    SUBMISSION_REVIEW {
        UUID id PK
        UUID submission_id FK
        UUID reviewed_by_id FK
        string action
        text comment
        datetime created_at
    }

    ORDER_UPDATE {
        int id PK
        text message
        UUID submission_id FK
        datetime created_at
    }

    REVIEW {
        UUID id PK
        UUID order_id FK
        UUID client_id FK
        UUID artist_id FK
        int rating
        text comment
        datetime created_at
    }

    DISPUTE {
        UUID id PK
        UUID order_id FK
        UUID raised_by_id FK
        text reason
        string status
        datetime created_at
    }

    PAYMENT {
        UUID id PK
        UUID order_id FK
        int amount
        string status
        string provider
        string provider_payment_id
        datetime released_at
        datetime refunded_at
        string provider_order_id
        datetime created_at
    }
```
