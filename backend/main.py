import io
import zipfile
import pandas as pd
from fastapi import FastAPI, UploadFile, File, HTTPException, Request, Response


app = FastAPI(docs_url=None, redoc_url=None)

@app.post("/")
async def csv(request: Request, file: UploadFile = File(...)):
    if file.content_type != "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        raise HTTPException(400, detail="Invalid document type")
    else:
        form = await request.form()
        columns = form.get("columns")
        content = await file.read()
        excel_data = pd.read_excel(io.BytesIO(content), sheet_name=None, usecols=columns)
        csv_files = []
        for sheet_name, df in excel_data.items():
            csv_data = df.to_csv(index=False)
            csv_files.append((sheet_name + ".csv", csv_data))

        zip_file = io.BytesIO()
        with zipfile.ZipFile(zip_file, mode="w", compression=zipfile.ZIP_DEFLATED) as zip_archive:
            for filename, data in csv_files:
                zip_archive.writestr(filename, data)

        zip_file.seek(0)
        return Response(content=zip_file.getvalue(), media_type="application/zip",
                        headers={"Content-Disposition": "attachment;filename=output.zip"})
