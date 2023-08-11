FROM public.ecr.aws/lambda/python:3.8
ARG FUNCTION_DIR="/function"

# copy the rest across
COPY app ${LAMBDA_TASK_ROOT}

# requirements as first operations (faster rebuilds)
COPY deploy/requirements.txt requirements.txt
RUN pip install --target ${LAMBDA_TASK_ROOT} -r requirements.txt

CMD [ "app.lambda_handler" ] 
