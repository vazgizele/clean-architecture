from datetime import date
import pytest

from src.domain.entities.atendente import Atendente
class TestAtendente:
    #id: int
    def test_id_not_is_integer(self):
        #Arrange
        atendente = Atendente("abc", "gizele", "18/01/1993", "21990724754", "21990724754", "gizele.costa@transfero.com")

        #Act
        with pytest.raises(Exception) as error:
            atendente.validade()

        #Assert
        assert str(error.value) == f'id must be a integer. [value={atendente.id}]'

    def test_id_not_is_positive(self):
        # Arrange
        atendente = Atendente(-1, "gizele", "18/01/1993", "21990724754", "21990724754", "gizele.costa@transfero.com")

        # Act
        with pytest.raises(Exception) as error:
            atendente.validade()
            
        # Assert
        assert str(error.value) == f'id must be a positive integer. [value={atendente.id}]'

    def test_name_is_not_string(self):
        #Arrange
        atendente = Atendente(1, 123, "18/01/1993", "21990724754", "21990724754", "gizele.costa@transfero.com")

        # Act
        with pytest.raises(Exception) as error:
            atendente.validade()
            
        # Assert
        assert str(error.value) == f"nome must be a string. [value={atendente.nome}]"

    def test_name_is_empty(self):
        #Arrange
        atendente = Atendente(1, "", "18/01/1993", "21990724754", "21990724754", "gizele.costa@transfero.com")

        # Act
        with pytest.raises(Exception) as error:
            atendente.validade()
            
        # Assert
        assert str(error.value) == f"nome must not be empty."

    def test_name_less_3(self):
        #Arrange
        atendente = Atendente(1, "ab", "18/01/1993", "21990724754", "21990724754", "gizele.costa@transfero.com")

        # Act
        with pytest.raises(Exception) as error:
            atendente.validade()
            
        # Assert
        assert str(error.value) == f'nome minimum size is - 3'

    def test_name_great_20(self):
        #Arrange
        atendente = Atendente(1, "gizele"*6, "18/01/1993", "21990724754", "21990724754", "gizele.costa@transfero.com")

        # Act
        with pytest.raises(Exception) as error:
            atendente.validade()
            
        # Assert
        assert str(error.value) == f'nome maximum size is - 30'
    
    def test_date_is_not_ok(self):
        #Arrange
        atendente = Atendente(1, "gizele", 123, "21990724754", "21990724754", "gizele.costa@transfero.com")

        # Act
        with pytest.raises(Exception) as error:
            atendente.validade()
            
        # Assert
        assert str(error.value) == f"data_nascimento must be a date. [value={atendente.data_nascimento}]"
    
    def test_phone_is_not_string(self):
        #Arrange
        atendente = Atendente(1, "gizele", date.today(), 21990724754, 21990724754, "gizele.costa@transfero.com")

        # Act
        with pytest.raises(Exception) as error:
            atendente.validade()
            
        # Assert
        assert str(error.value) == f"telefone1 must be a string. [value={atendente.telefone1}]"
    
    def test_phone_is_not_format(self):
        #Arrange
        atendente = Atendente(1, "gizele", date.today(), '*90724754', None, "gizele.costa@transfero.com")

        # Act
        with pytest.raises(Exception) as error:
            atendente.validade()
            
        # Assert
        assert str(error.value) == f'telefone1 must be in format [123456789], [value={atendente.telefone1}]'

    def test_email_is_not_none(self):
        #Arrange
        atendente = Atendente(1, "gizele", date.today(), '21990724754', '21990724754', None)

        # Act
        with pytest.raises(Exception) as error:
            atendente.validade()
            
        # Assert
        assert str(error.value) == f"invalid E-mail. [value=]"
    
    def test_email_is_not_string(self):
        #Arrange
        atendente = Atendente(1, "gizele", date.today(), '21990724754', '21990724754',123456789)

        # Act
        with pytest.raises(Exception) as error:
            atendente.validade()
            
        # Assert
        assert str(error.value) == f"email must be a string. [value={atendente.email}]"

    def test_email_is_not_format(self):
        #Arrange
        atendente = Atendente(1, "gizele", date.today(), '21990724754', '21990724754',"gizele.costa@.com")

        # Act
        with pytest.raises(Exception) as error:
            atendente.validade()
            
        # Assert
        assert str(error.value) == f"email must be in format [User@Domain.com.br[br=Optional], [value={atendente.email}]"