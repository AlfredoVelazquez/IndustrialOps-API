from sqlalchemy import text

from app.database.connection import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT @@VERSION"))

        for row in result:
            print("\n✅ Conexión exitosa a SQL Server\n")
            print(row[0])

except Exception as e:
    print("\n❌ Error de conexión:\n")
    print(e)