console.log("Hello World")

// P1

// Define the recursive utility type
type DeepPartial<T> = {
    [P in keyof T]?: T[P] extends Array<infer U>
      ? Array<DeepPartial<U>> // Handle arrays recursively
      : T[P] extends object
      ? DeepPartial<T[P]> // Handle nested objects recursively
      : T[P]; // Base case
  };
  
  // Example Usage
  type Example = {
    name: string;
    age: number;
    nested: {
      hobbies: string[];
      details: {
        address: string;
        phone: number;
      };
    };
  };
  
  const data: DeepPartial<Example> = {
    name: "John",
    nested: {
      hobbies: ["reading"],
      details: {
        address: "123 Main St",
      },
    },
  };

// P2 
// Define types for table schema
type TableSchema = {
    id: number;
    name: string;
    age: number;
    isActive: boolean;
  };
  
  // Valid operators for each type
  type Operators<T> = T extends number
    ? "=" | ">" | "<"
    : T extends string
    ? "=" | "LIKE"
    : T extends boolean
    ? "="
    : never;
  
  // Query Builder Type
  type Filter<T> = {
    [K in keyof T]?: {
      operator: Operators<T[K]>;
      value: T[K];
    };
  };
  
  // Example Usage
  const userQuery: Filter<TableSchema> = {
    id: { operator: "=", value: 1 },
    name: { operator: "LIKE", value: "John%" },
    isActive: { operator: "=", value: true },
  };

  // P3
  // Define overload signatures
function handleCallback<T>(callback: () => T extends Promise<any> ? T : T): T;

// Implementation
function handleCallback<T>(callback: () => T): T {
  return callback();
}

// Example Usage
const syncResult = handleCallback(() => 42); // inferred as number
const asyncResult = handleCallback(async () => "Hello"); // inferred as Promise<string>

// Example output
console.log(syncResult); // 42
asyncResult.then(result => console.log(result)); // "Hello"
