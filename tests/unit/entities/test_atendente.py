from datetime import date
import pytest

from src.domain.entities.atendente import Atendente


class TestAtendente:
    #id: int
    def test_id_integer(self):
        #Arrange
        atendente = Atendente("abc", "gizele", "18/01/1993", "21990724754", "21990724754", "gizele.costa@transfero.com")

        #Act
        with pytest.raises(Exception) as error:
            atendente.validade()

        #Assert
        assert str(error.value) == f'id must be a integer. [value={atendente.id}]'

    def test_id_positive(self):
        # Arrange
        atendente = Atendente(-1, "gizele", "18/01/1993", "21990724754", "21990724754", "gizele.costa@transfero.com")

        # Act
        with pytest.raises(Exception) as error:
            atendente.validade()
            
        # Assert
        assert str(error.value) == f'id must be a positive integer. [value={atendente.id}]'