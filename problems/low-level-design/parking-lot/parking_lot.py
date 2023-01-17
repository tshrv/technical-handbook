"""
Parking Lot, Entry Point and Exit Point
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import uuid4


class TicketStatus(Enum):
    OPEN = 'open'
    CLOSED = 'closed'


class TicketNotFoundException(Exception):
    """
    Ticket with mentioned attributes does not exist
    """
    pass


class OpenTicketExistsException(Exception):
    """
    An open ticket for the mentioned vehicle already exists
    """
    pass


class ClosedTicketException(Exception):
    """
    Attempting to close an already closed ticket
    """
    pass


@dataclass
class Vehicle:
    registration_number: str


@dataclass
class Ticket:
    id: uuid4 = field(init=False)
    vehicle: Vehicle
    closed_at: Optional[datetime] = field(init=False, default=None)
    created_at: datetime = field(init=False)
    status: TicketStatus = field(default=TicketStatus.OPEN)

    def __post_init__(self):
        self.id = uuid4()
        self.created_at = datetime.now()

 
class TicketCRUD:
    def get(self, ticket_id: str) -> Ticket:
        """
        return the ticket object with ticket_id
        raises TicketNotFoundException if ticket_id does not exist
        """
        ...

    def vehicle_open_ticket_exists(self, vehicle: Vehicle) -> bool:
        """check if an open ticket exists for the mentioned vehicle"""
        ...
    
    def create(self, vehicle: Vehicle) -> Ticket:
        """create a new ticket for the mentioned vehicle"""
        ...
    
    def update(self, ticket: Ticket) -> Ticket:
        """update the ticket with id ticket.id to the new attributes
        Raises TicketNotFoundException if ticket with the mentioned id not found"""
        ...
    
    def delete(self, ticket: Ticket) -> Ticket:
        ...
    

DEFAULT_TICKET_CRUD_CLASS = TicketCRUD


class TicketProcessor:
    def __init__(self) -> None:
        self.ticket_crud = DEFAULT_TICKET_CRUD_CLASS()
    
    def create(self, vehicle: Vehicle) -> Ticket:
        """
        if an open ticket exists for the vehicle, raises OpenTicketExistsException
        otherwise, creates and returns a new ticket in open state
        """
        if self.ticket_crud.vehicle_open_ticket_exists(vehicle):
            raise OpenTicketExistsException()
        return self.ticket_crud.create(vehicle)

    def close(self, ticket_id: str) -> Ticket:
        """if the ticket is not in open state, raises TicketClosedException
        Otherwise, closes the ticket"""
        ticket = self.ticket_crud.get(ticket_id)    # get object or TicketNotFoundException
        if ticket.status == TicketStatus.CLOSED:
            raise ClosedTicketException()

        ticket.status = TicketStatus.CLOSED
        ticket.closed_at = datetime.now()
        ticket = self.ticket_crud.update(ticket)
        return ticket


DEFAULT_TICKET_PROCESSOR_CLASS = TicketProcessor


class EntryPoint:
    def __init__(self) -> None:
        self.ticket_processor = DEFAULT_TICKET_PROCESSOR_CLASS()

    def register_vehicle_entry(self, vehicle: Vehicle) -> Ticket:
        ticket = self.ticket_processor.create(vehicle)
        return ticket


class ExitPoint:
    def __init__(self) -> None:
        self.ticket_processor = DEFAULT_TICKET_PROCESSOR_CLASS()
    
    def register_vehicle_exit(self, ticket_id: str) -> Ticket:
        ticket = self.ticket_processor.close(ticket_id)
        return ticket