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

    @pytest.mark.parametrize("id, nome, data_nascimento, telefone1, telefone2, email, msg_expected", [
       ("abc", "gizele", "18/01/1993", "21990724754", "21990724754", "gizele.costa@transfero.com", 'id must be a integer. [value=abc]' ),
       (-1, "gizele", "18/01/1993", "21990724754", "21990724754", "gizele.costa@transfero.com", 'id must be a positive integer. [value=-1]'),
       (1, 123, "18/01/1993", "21990724754", "21990724754", "gizele.costa@transfero.com", "nome must be a string. [value=123]"),
       (1, "", "18/01/1993", "21990724754", "21990724754", "gizele.costa@transfero.com", "nome must not be empty."),
       (1, "ab", "18/01/1993", "21990724754", "21990724754", "gizele.costa@transfero.com",'nome minimum size is - 3'),
       (1, "gizele"*6, "18/01/1993", "21990724754", "21990724754", "gizele.costa@transfero.com",'nome maximum size is - 30'),
       (1, "gizele", 123, "21990724754", "21990724754", "gizele.costa@transfero.com","data_nascimento must be a date. [value=123]"),
       (1, "gizele", date.today(), 21990724754, 21990724754, "gizele.costa@transfero.com", "telefone1 must be a string. [value=21990724754]"),
       (1, "gizele", date.today(), '*90724754', None, "gizele.costa@transfero.com",'telefone1 must be in format [123456789], [value=*90724754]'),
       (1, "gizele", date.today(), '21990724754', '21990724754', None,"invalid E-mail. [value=]"),
       (1, "gizele", date.today(), '21990724754', '21990724754',123456789,"email must be a string. [value=123456789]"),
       (1, "gizele", date.today(), '21990724754', '21990724754',"gizele.costa@.com","email must be in format [User@Domain.com.br[br=Optional], [value=gizele.costa@.com]")
      
    ])
    def test_all(self, id, nome, data_nascimento, telefone1, telefone2, email, msg_expected):
        # Arrange
        atendente = Atendente(id, nome, data_nascimento, telefone1, telefone2, email)

        # Act
        with pytest.raises(Exception) as error:
            atendente.validade()
            
        # Assert
        assert str(error.value) == msg_expected