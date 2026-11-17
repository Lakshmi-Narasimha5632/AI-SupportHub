
# AI SupportHub - Database Design

## 1. Database Overview

Database: MySQL

The database stores user accounts, customer information, agents, tickets, categories, FAQs, notifications, and analytics-related information.

## 2. Main Database Tables

### 2.1 Users

Table Name: accounts_user

Purpose:
Stores authentication details and user roles.

Fields:

| Field | Type | Description |
|---|---|---|
| id | BigAutoField | Primary key |
| email | EmailField | Unique email |
| full_name | CharField | User's name |
| password | Password | Hashed password |
| role | CharField | CUSTOMER / AGENT / ADMIN |
| auth_provider | CharField | EMAIL / GOOGLE |
| is_active | Boolean | Account status |
| is_staff | Boolean | Admin access flag |
| date_joined | DateTime | Registration date |
| created_at | DateTime | Creation timestamp |
| updated_at | DateTime | Last update |

### 2.2 Customers

Purpose:
Stores additional customer profile information.

Planned fields:
- id
- user_id (Foreign Key)
- phone_number
- company_name
- address
- created_at

### 2.3 Agents

Purpose:
Stores support agent information.

Planned fields:
- id
- user_id (Foreign Key)
- department
- designation
- availability_status
- created_at

### 2.4 Categories

Purpose:
Stores ticket categories.

Planned fields:
- id
- name
- description
- ticket_prefix
- is_active
- created_at

Examples:
- TECH - Technical Support
- BILL - Billing
- ACC - Account Issues
- GEN - General Enquiry

### 2.5 Tickets

Purpose:
Stores customer support tickets.

Planned fields:
- id
- ticket_number
- customer_id (Foreign Key)
- category_id (Foreign Key)
- assigned_agent_id (Foreign Key, nullable)
- subject
- description
- status
- priority
- sentiment
- created_at
- updated_at
- resolved_at

Possible statuses:
- OPEN
- IN_PROGRESS
- WAITING_FOR_CUSTOMER
- RESOLVED
- CLOSED

Possible priorities:
- LOW
- MEDIUM
- HIGH
- URGENT

### 2.6 Ticket Comments

Purpose:
Stores conversations and replies related to tickets.

Planned fields:
- id
- ticket_id (Foreign Key)
- user_id (Foreign Key)
- message
- is_internal
- created_at

### 2.7 FAQs

Purpose:
Stores frequently asked questions and answers.

Planned fields:
- id
- question
- answer
- category_id (Foreign Key)
- is_active
- created_at
- updated_at

### 2.8 Notifications

Purpose:
Stores notifications sent to users.

Planned fields:
- id
- user_id (Foreign Key)
- title
- message
- notification_type
- is_read
- created_at

### 2.9 Ticket AI Analysis

Purpose:
Stores AI-generated ticket analysis.

Planned fields:
- id
- ticket_id (Foreign Key)
- predicted_category
- predicted_priority
- sentiment
- summary
- suggested_response
- confidence_score
- created_at

### 2.10 Audit Logs

Purpose:
Tracks important actions performed by users.

Planned fields:
- id
- user_id (Foreign Key)
- action
- entity_type
- entity_id
- details
- created_at

## 3. Table Relationships

- One User can have one Customer profile.
- One User can have one Agent profile.
- One Customer can create many Tickets.
- One Category can contain many Tickets.
- One Agent can handle many Tickets.
- One Ticket can have many Comments.
- One Category can contain many FAQs.
- One User can receive many Notifications.
- One Ticket can have multiple AI analysis records.

## 4. Database Constraints

- Email must be unique.
- Ticket number must be unique.
- Foreign keys maintain relationships.
- Required fields cannot be NULL.
- Ticket status and priority must use valid choices.
- Customer and agent profiles must reference valid users.

## 5. Indexing Strategy

Recommended indexes:
- users.email
- tickets.ticket_number
- tickets.status
- tickets.priority
- tickets.customer_id
- tickets.assigned_agent_id
- tickets.created_at

## 6. Notes

This document describes the planned database structure.

Update field types, constraints, and relationships according to the actual Django models and migrations.
