import os
import pymssql
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    server = os.getenv("AZURE_SQL_SERVER")
    database = os.getenv("AZURE_SQL_DB")
    username = os.getenv("AZURE_SQL_USER")
    password = os.getenv("AZURE_SQL_PASSWORD")
    return pymssql.connect(
        server=server,
        user=username,
        password=password,
        database=database,
        port=1433
    )
###original 
###
'''def fetch_activity_data(
    customer_id=10,
    activity_type=None,
    since_days=365
) -> pd.DataFrame:
    """
    获取指定客户最近一年的活动数据（可指定类型），为所有agent提供原始数据。
    """
    conn = get_connection()
    query = """
        SELECT ActivityID, CustomerID, Type, StartTime, EndTime, Duration,
               StartCondition, StartLocation, EndCondition, Notes
        FROM dbo.Activity
        WHERE CustomerID = %s AND StartTime >= DATEADD(day, -%s, GETDATE())
    """
    params = [customer_id, since_days]
    if activity_type:
        query += " AND Type = %s"
        params.append(activity_type)
    query += " ORDER BY StartTime ASC"
    df = pd.read_sql(query, conn, params=params)
    conn.close()
    return df'''
    
import os
import pandas as pd

def fetch_activity_data(
    customer_id=10,
    activity_type=None,
    since_days=365
) -> pd.DataFrame:
    if os.environ.get("DISABLE_DB", "false").lower() == "true":
        # 用空 DataFrame 返回，防止部署时访问数据库
        return pd.DataFrame()

    try:
        conn = get_connection()
        query = """
            SELECT ActivityID, CustomerID, Type, StartTime, EndTime, Duration,
                   StartCondition, StartLocation, EndCondition, Notes
            FROM dbo.Activity
            WHERE CustomerID = %s AND StartTime >= DATEADD(day, -%s, GETDATE())
        """
        params = [customer_id, since_days]
        if activity_type:
            query += " AND Type = %s"
            params.append(activity_type)
        query += " ORDER BY StartTime ASC"
        df = pd.read_sql(query, conn, params=params)
        conn.close()
        return df
    except Exception as e:
        print("DB connection failed:", e)
        return pd.DataFrame()
# 处理数据库连接异常，返回空 DataFrame
# 这样可以在部署时避免访问数据库导致的错误
# 你可以通过设置环境变量 DISABLE_DB=true 来禁用数据库访问
# 这在部署到 Vertex AI 时非常有用，避免因数据库不可用而导致部署失败
# 例如在 Vertex AI 的环境变量设置中添加 DISABLE_DB=true
# 这样在部署时就不会尝试连接数据库，而是返回一个空的 Data