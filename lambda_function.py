import logging

# Setup logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        # Simple test log to ensure logging is working
        logger.info("Lambda function execution started.")

        # Simulating some basic Python functionality
        numbers = [1, 2, 3, 4, 5]
        total = sum(numbers)
        logger.info(f"The total sum of numbers is: {total}")

        # Return success response
        return {
            'statusCode': 200,
            'body': 'Test passed: Simple Python operations executed successfully.'
        }

    except Exception as e:
        # Log any exception that occurs
        logger.error(f"Test failed: {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Test failed: {str(e)}"
        }
