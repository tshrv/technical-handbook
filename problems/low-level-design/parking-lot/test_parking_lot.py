"""
Test ParkingLot's EntryPoint and ExitPoint
"""
import pytest
from parking_lot import ExitPoint, Ticket, TicketNotFoundException, TicketStatus, Vehicle, EntryPoint, TicketProcessor, TicketCRUD, \
    OpenTicketExistsException

@pytest.fixture
def tickets_data():
    tickets = [
        Ticket(vehicle=Vehicle('UP32KZ4474')),      # existing
        Ticket(vehicle=Vehicle('UP32JS8920')),      # existing
        Ticket(vehicle=Vehicle('UP70BP8048')),      # existing
        # Ticket(vehicle=Vehicle('UP32KZ8884')),      # non-existing
    ]
    yield tickets

@pytest.fixture
def entry_point():
    entry_point_obj = EntryPoint()
    yield entry_point_obj

@pytest.fixture
def exit_point():
    exit_point_obj = ExitPoint()
    yield exit_point_obj


class TestEntryPoint:
    @pytest.mark.parametrize(('vehicle_registration_number',), (('UP32KZ8884',),))
    def test_register_vehicle_entry_non_existing(self, entry_point: EntryPoint, vehicle_registration_number: str):
        ticket = entry_point.register_vehicle_entry(Vehicle(vehicle_registration_number))
        assert isinstance(ticket, Ticket)

    @pytest.mark.parametrize(('vehicle_registration_number',), (('UP70BP8048',),))
    def test_register_vehicle_entry_existing(self, entry_point: EntryPoint, vehicle_registration_number: str):
        with pytest.raises(OpenTicketExistsException):
            ticket = entry_point.register_vehicle_entry(Vehicle(vehicle_registration_number))


class TestExitPoint:
    @pytest.mark.parametrize(('vehicle_registration_number',), (('UP32KZ8884',),))
    def test_register_vehicle_exit_existing(self, exit_point: ExitPoint, 
        vehicle_registration_number: str):
        """exit processing for a valid ticket id"""
        ticket = exit_point.register_vehicle_exit(Vehicle(vehicle_registration_number))
        assert isinstance(ticket, Ticket)
        assert ticket.status == TicketStatus.CLOSED

    @pytest.mark.parametrize(('vehicle_registration_number',), (('UP70BP8048',),))
    def test_register_vehicle_exit_non_existing(self, exit_point: ExitPoint, 
        vehicle_registration_number: str):
        """exit processing for an invalid / non-existing ticket id"""
        with pytest.raises(TicketNotFoundException):
            ticket = exit_point.register_vehicle_exit(Vehicle(vehicle_registration_number))
    
    @pytest.mark.parametrize(('vehicle_registration_number',), (('UP70BP8048',),))
    def test_register_vehicle_exit_already_closed(self,  exit_point: ExitPoint, 
        vehicle_registration_number: str):
        """exit processing for an already closed ticket"""
        with pytest.raises(OpenTicketExistsException):
            ticket = exit_point.register_vehicle_exit(Vehicle(vehicle_registration_number))
    
